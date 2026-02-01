# 📈 Investing BBS

A retro BBS-style terminal interface for browsing financial markets data from investing.com and other sources.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)

## 🎮 Screenshot

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                              MARKET OVERVIEW                                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────────┐
│                              Major Indices                                   │
├────────────┬─────────────────────────┬────────────────┬────────────┬─────────┤
│ Symbol     │ Name                    │          Price │     Change │       % │
├────────────┼─────────────────────────┼────────────────┼────────────┼─────────┤
│ SPX        │ S&P 500                 │       4,200.50 │   +15.30   │ +0.37%  │
│ DJI        │ Dow Jones               │      34,500.20 │  +120.50   │ +0.35%  │
│ IXIC       │ Nasdaq                  │      13,800.75 │   +85.20   │ +0.62%  │
│ FTSE       │ FTSE 100                │       7,650.30 │   -12.40   │ -0.16%  │
│ DAX        │ DAX 40                  │      15,800.15 │   +45.80   │ +0.29%  │
│ N225       │ Nikkei 225              │      28,500.60 │   -85.30   │ -0.30%  │
└────────────┴─────────────────────────┴────────────────┴────────────┴─────────┘

╔══════════════════════════════════════════════════════════════════════════════╗
║ User: Guest | 2026-02-01 14:30:00                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## ✨ Features

- 🎯 **BBS-style retro interface** - Nostalgic terminal UI with box-drawing characters
- 📊 **Real-time market data** - Live prices from Yahoo Finance
- 💱 **Multiple asset classes**:
  - Stock Market Indices (S&P 500, Dow Jones, Nasdaq, etc.)
  - Cryptocurrencies (Bitcoin, Ethereum, etc.)
  - Forex/Currency pairs
  - Commodities (Gold, Silver, Oil, etc.)
  - World Stock Indices
  - Individual Stock Search
- 🖥️ **Cross-platform** - Works on Linux, macOS, and Windows
- ⚡ **Fast and lightweight** - Pure Python, minimal dependencies

## 🚀 Installation

### Quick Install (Recommended)

One-line installation with curl:

```bash
curl -fsSL https://raw.githubusercontent.com/hsuanchenlin/investing_cli/main/install.sh | bash
```

This will:
- ✅ Check Python version (requires 3.7+)
- ✅ Create an isolated virtual environment
- ✅ Install all dependencies
- ✅ Set up the `investing-bbs` command
- ✅ Install to `~/.local/bin` (no sudo required)

### Alternative Methods

<details>
<summary>Install from PyPI</summary>

```bash
pip install investing-bbs
```
</details>

<details>
<summary>Install from Source</summary>

```bash
# Clone the repository
git clone https://github.com/hsuanchenlin/investing_cli.git
cd investing_cli

# Install
pip install -e .
```
</details>

<details>
<summary>Direct install with pip</summary>

```bash
pip install git+https://github.com/hsuanchenlin/investing_cli.git
```
</details>

### Uninstall

If you installed with curl:

```bash
rm -rf ~/.local/share/investing-bbs
rm ~/.local/bin/investing-bbs
```

If you installed with pip:

```bash
pip uninstall investing-bbs
```

## 🎮 Usage

### Launch the BBS interface

```bash
investing-bbs
```

### Show version

```bash
investing-bbs --version
```

### Navigation

Once inside the BBS:

| Key | Action |
|-----|--------|
| `1` | Market Overview |
| `2` | Cryptocurrency |
| `3` | Forex |
| `4` | Commodities |
| `5` | World Indices |
| `6` | Search Stocks |
| `R` | Refresh data |
| `Q` | Quit |
| `Enter` | Return to menu |

## 🛠️ Requirements

- Python 3.7 or higher
- Terminal with Unicode support (for box-drawing characters)

### Dependencies

- `rich` - Terminal formatting and tables
- `requests` - HTTP requests for market data
- `python-dateutil` - Date handling

## 📝 Example Session

```bash
$ investing-bbs

╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██╗███╗   ██╗██╗   ██╗███████╗███████╗████████╗██╗███╗   ██╗               ║
║   ...
║                                                                              ║
║                    Press ENTER to continue...                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

# Main Menu appears...
[?] Select option: 2

# Shows cryptocurrency prices with live data...
```

## 🔧 Development

### Setup development environment

```bash
git clone https://github.com/linproxy/investing-com-cli.git
cd investing-com-cli
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### Project Structure

```
investing-com-cli/
├── investing_bbs/          # Main package
│   ├── __init__.py
│   ├── main.py             # CLI entry point
│   ├── ui.py               # BBS-style UI components
│   └── api.py              # Market data API
├── investing-bbs.py        # Alternative entry point
├── setup.py                # Package configuration
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## 📊 Data Sources

This tool fetches market data from:
- **Yahoo Finance API** - Real-time stock, crypto, and forex data
- **Mock data fallback** - Demo data when API is unavailable

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic BBS systems and PTT.cc
- Built with [Rich](https://github.com/Textualize/rich) for beautiful terminal output
- Market data provided by Yahoo Finance

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. The data provided may be delayed or inaccurate. Always verify financial data from official sources before making investment decisions.

---

**Enjoy your retro trading experience!** 📉📈
