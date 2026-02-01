#!/usr/bin/env bash

# investing-bbs installer script
# Usage: curl -fsSL https://raw.githubusercontent.com/hsuanchenlin/investing_cli/main/install.sh | bash

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_URL="https://github.com/hsuanchenlin/investing_cli"
INSTALL_DIR="$HOME/.local/share/investing-bbs"
BIN_DIR="$HOME/.local/bin"
VENV_DIR="$INSTALL_DIR/venv"

# Print colored message
print_msg() {
    local color=$1
    shift
    echo -e "${color}$@${NC}"
}

print_success() { print_msg "$GREEN" "✓ $@"; }
print_error() { print_msg "$RED" "✗ $@"; }
print_info() { print_msg "$BLUE" "→ $@"; }
print_warning() { print_msg "$YELLOW" "⚠ $@"; }

# Print header
print_header() {
    echo ""
    print_msg "$BLUE" "╔══════════════════════════════════════════════════════════════════╗"
    print_msg "$BLUE" "║                                                                  ║"
    print_msg "$BLUE" "║               📈 Investing BBS Installer                         ║"
    print_msg "$BLUE" "║                                                                  ║"
    print_msg "$BLUE" "╚══════════════════════════════════════════════════════════════════╝"
    echo ""
}

# Check Python version
check_python() {
    print_info "Checking Python installation..."

    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed"
        print_info "Please install Python 3.7 or higher from https://www.python.org"
        exit 1
    fi

    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    PYTHON_MAJOR=$(python3 -c 'import sys; print(sys.version_info.major)')
    PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')

    if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 7 ]); then
        print_error "Python 3.7 or higher is required (found $PYTHON_VERSION)"
        exit 1
    fi

    print_success "Python $PYTHON_VERSION found"
}

# Check if git is installed
check_git() {
    if ! command -v git &> /dev/null; then
        print_error "git is not installed"
        print_info "Please install git from https://git-scm.com"
        exit 1
    fi
}

# Create installation directory
create_install_dir() {
    print_info "Creating installation directory..."

    # Remove old installation if exists
    if [ -d "$INSTALL_DIR" ]; then
        print_warning "Removing previous installation..."
        rm -rf "$INSTALL_DIR"
    fi

    mkdir -p "$INSTALL_DIR"
    mkdir -p "$BIN_DIR"

    print_success "Installation directory created"
}

# Clone or download the repository
download_repo() {
    print_info "Downloading investing-bbs..."

    cd "$INSTALL_DIR"

    if command -v git &> /dev/null; then
        git clone --depth 1 "$REPO_URL" source 2>/dev/null || {
            print_error "Failed to clone repository"
            exit 1
        }
    else
        print_error "git is required for installation"
        exit 1
    fi

    print_success "Downloaded successfully"
}

# Create virtual environment
create_venv() {
    print_info "Creating virtual environment..."

    python3 -m venv "$VENV_DIR" || {
        print_error "Failed to create virtual environment"
        exit 1
    }

    print_success "Virtual environment created"
}

# Install package
install_package() {
    print_info "Installing investing-bbs and dependencies..."

    # Activate virtual environment and install
    . "$VENV_DIR/bin/activate"

    pip install --quiet --upgrade pip
    pip install --quiet -e "$INSTALL_DIR/source" || {
        print_error "Failed to install package"
        exit 1
    }

    deactivate

    print_success "Package installed"
}

# Create wrapper script
create_wrapper() {
    print_info "Creating executable wrapper..."

    cat > "$BIN_DIR/investing-bbs" << 'EOF'
#!/usr/bin/env bash
VENV_DIR="$HOME/.local/share/investing-bbs/venv"
. "$VENV_DIR/bin/activate"
python -m investing_bbs.main "$@"
deactivate
EOF

    chmod +x "$BIN_DIR/investing-bbs"

    print_success "Wrapper created"
}

# Add to PATH instructions
show_path_instructions() {
    echo ""

    # Check if BIN_DIR is in PATH
    if [[ ":$PATH:" == *":$BIN_DIR:"* ]]; then
        print_success "Installation complete!"
    else
        print_warning "Installation complete, but $BIN_DIR is not in your PATH"
        echo ""
        print_info "Add the following line to your shell profile:"
        echo ""

        if [ -n "$ZSH_VERSION" ]; then
            SHELL_RC="$HOME/.zshrc"
        elif [ -n "$BASH_VERSION" ]; then
            SHELL_RC="$HOME/.bashrc"
        else
            SHELL_RC="$HOME/.profile"
        fi

        echo "    export PATH=\"\$HOME/.local/bin:\$PATH\""
        echo ""
        print_info "Then restart your shell or run:"
        echo "    source $SHELL_RC"
        echo ""
    fi
}

# Show usage
show_usage() {
    echo ""
    print_msg "$GREEN" "╔══════════════════════════════════════════════════════════════════╗"
    print_msg "$GREEN" "║                       🎮 Quick Start                             ║"
    print_msg "$GREEN" "╚══════════════════════════════════════════════════════════════════╝"
    echo ""
    print_info "Launch the BBS:"
    echo "    investing-bbs"
    echo ""
    print_info "Show version:"
    echo "    investing-bbs --version"
    echo ""
    print_info "Uninstall:"
    echo "    rm -rf ~/.local/share/investing-bbs"
    echo "    rm ~/.local/bin/investing-bbs"
    echo ""
}

# Main installation
main() {
    print_header

    check_python
    check_git
    create_install_dir
    download_repo
    create_venv
    install_package
    create_wrapper
    show_path_instructions
    show_usage

    print_success "Ready to trade! 📈📉"
    echo ""
}

# Run main installation
main
