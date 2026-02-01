"""
Investing.com API wrapper
Fetches financial data from various sources
"""

import requests
import json
from datetime import datetime
from typing import List, Dict, Optional

class InvestingAPI:
    """API wrapper for fetching financial market data"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def _get(self, url: str, params: dict = None) -> dict:
        """Make GET request with error handling"""
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # Return mock data on failure
            return self._get_mock_data()
            
    def _get_mock_data(self) -> List[Dict]:
        """Return mock data when API is unavailable"""
        return [
            {"symbol": "SPX", "name": "S&P 500", "price": 4200.50, "change": 15.30, "change_pct": 0.37},
            {"symbol": "DJI", "name": "Dow Jones", "price": 34500.20, "change": 120.50, "change_pct": 0.35},
            {"symbol": "IXIC", "name": "Nasdaq", "price": 13800.75, "change": 85.20, "change_pct": 0.62},
            {"symbol": "FTSE", "name": "FTSE 100", "price": 7650.30, "change": -12.40, "change_pct": -0.16},
            {"symbol": "DAX", "name": "DAX 40", "price": 15800.15, "change": 45.80, "change_pct": 0.29},
            {"symbol": "N225", "name": "Nikkei 225", "price": 28500.60, "change": -85.30, "change_pct": -0.30},
        ]
        
    def get_major_indices(self) -> List[Dict]:
        """Get major stock market indices"""
        # Using Yahoo Finance API as fallback
        symbols = ["^GSPC", "^DJI", "^IXIC", "^FTSE", "^GDAXI", "^N225", "^HSI", "^FCHI"]
        names = {
            "^GSPC": "S&P 500",
            "^DJI": "Dow Jones",
            "^IXIC": "Nasdaq",
            "^FTSE": "FTSE 100",
            "^GDAXI": "DAX 40",
            "^N225": "Nikkei 225",
            "^HSI": "Hang Seng",
            "^FCHI": "CAC 40"
        }
        
        try:
            return self._fetch_yahoo_data(symbols, names)
        except:
            return self._get_mock_data()
            
    def get_crypto(self) -> List[Dict]:
        """Get cryptocurrency prices"""
        symbols = ["BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "ADA-USD", "DOGE-USD", "SOL-USD"]
        names = {
            "BTC-USD": "Bitcoin",
            "ETH-USD": "Ethereum",
            "BNB-USD": "BNB",
            "XRP-USD": "XRP",
            "ADA-USD": "Cardano",
            "DOGE-USD": "Dogecoin",
            "SOL-USD": "Solana"
        }
        
        try:
            return self._fetch_yahoo_data(symbols, names)
        except:
            # Fallback mock data
            return [
                {"symbol": "BTC", "name": "Bitcoin", "price": 43500.00, "change": 850.50, "change_pct": 1.99},
                {"symbol": "ETH", "name": "Ethereum", "price": 2600.75, "change": 45.20, "change_pct": 1.77},
                {"symbol": "BNB", "name": "BNB", "price": 315.40, "change": 5.80, "change_pct": 1.87},
                {"symbol": "XRP", "name": "XRP", "price": 0.62, "change": 0.02, "change_pct": 3.33},
                {"symbol": "ADA", "name": "Cardano", "price": 0.58, "change": 0.01, "change_pct": 1.75},
                {"symbol": "DOGE", "name": "Dogecoin", "price": 0.09, "change": 0.00, "change_pct": 0.00},
                {"symbol": "SOL", "name": "Solana", "price": 98.50, "change": 4.20, "change_pct": 4.45},
            ]
            
    def get_forex(self) -> List[Dict]:
        """Get forex currency pairs"""
        symbols = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "USDCHF=X", "AUDUSD=X", "USDCAD=X"]
        names = {
            "EURUSD=X": "EUR/USD",
            "GBPUSD=X": "GBP/USD",
            "USDJPY=X": "USD/JPY",
            "USDCHF=X": "USD/CHF",
            "AUDUSD=X": "AUD/USD",
            "USDCAD=X": "USD/CAD"
        }
        
        try:
            return self._fetch_yahoo_data(symbols, names)
        except:
            return [
                {"symbol": "EUR/USD", "name": "Euro/Dollar", "price": 1.0850, "change": 0.0020, "change_pct": 0.18},
                {"symbol": "GBP/USD", "name": "Pound/Dollar", "price": 1.2650, "change": 0.0035, "change_pct": 0.28},
                {"symbol": "USD/JPY", "name": "Dollar/Yen", "price": 148.50, "change": -0.25, "change_pct": -0.17},
                {"symbol": "USD/CHF", "name": "Dollar/Franc", "price": 0.8650, "change": 0.0010, "change_pct": 0.12},
                {"symbol": "AUD/USD", "name": "Aussie/Dollar", "price": 0.6550, "change": 0.0040, "change_pct": 0.61},
                {"symbol": "USD/CAD", "name": "Dollar/Loony", "price": 1.3450, "change": -0.0020, "change_pct": -0.15},
            ]
            
    def get_commodities(self) -> List[Dict]:
        """Get commodity prices"""
        symbols = ["GC=F", "SI=F", "CL=F", "NG=F", "ZC=F", "ZW=F"]
        names = {
            "GC=F": "Gold",
            "SI=F": "Silver",
            "CL=F": "Crude Oil",
            "NG=F": "Natural Gas",
            "ZC=F": "Corn",
            "ZW=F": "Wheat"
        }
        
        try:
            return self._fetch_yahoo_data(symbols, names)
        except:
            return [
                {"symbol": "GOLD", "name": "Gold (oz)", "price": 2050.50, "change": 12.30, "change_pct": 0.60},
                {"symbol": "SILVER", "name": "Silver (oz)", "price": 23.15, "change": 0.35, "change_pct": 1.54},
                {"symbol": "OIL", "name": "Crude Oil (bbl)", "price": 75.80, "change": 1.20, "change_pct": 1.61},
                {"symbol": "GAS", "name": "Natural Gas", "price": 2.85, "change": -0.05, "change_pct": -1.72},
                {"symbol": "CORN", "name": "Corn (bushel)", "price": 4.75, "change": 0.02, "change_pct": 0.42},
                {"symbol": "WHEAT", "name": "Wheat (bushel)", "price": 6.20, "change": 0.08, "change_pct": 1.31},
            ]
            
    def get_world_indices(self) -> List[Dict]:
        """Get world stock indices"""
        return self.get_major_indices()
        
    def search_stock(self, symbol: str) -> List[Dict]:
        """Search for a stock by symbol"""
        symbol_upper = symbol.upper()
        
        try:
            # Try to fetch from Yahoo Finance
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol_upper}"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                chart = data.get('chart', {})
                result = chart.get('result', [{}])[0]
                meta = result.get('meta', {})
                
                price = meta.get('regularMarketPrice', 0)
                prev_close = meta.get('previousClose', price)
                change = price - prev_close
                change_pct = (change / prev_close * 100) if prev_close else 0
                name = meta.get('shortName', meta.get('longName', symbol_upper))
                
                return [{
                    "symbol": symbol_upper,
                    "name": name,
                    "price": price,
                    "change": change,
                    "change_pct": change_pct
                }]
        except:
            pass
            
        # Return not found
        return []
        
    def _fetch_yahoo_data(self, symbols: list, names: dict) -> List[Dict]:
        """Fetch data from Yahoo Finance"""
        results = []
        
        for symbol in symbols:
            try:
                url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
                response = self.session.get(url, timeout=5)
                
                if response.status_code == 200:
                    data = response.json()
                    chart = data.get('chart', {})
                    result = chart.get('result', [{}])[0]
                    meta = result.get('meta', {})
                    
                    price = meta.get('regularMarketPrice', 0)
                    prev_close = meta.get('previousClose', price)
                    change = price - prev_close
                    change_pct = (change / prev_close * 100) if prev_close else 0
                    
                    clean_symbol = symbol.replace('^', '').replace('=X', '').replace('-USD', '').replace('=F', '')
                    
                    results.append({
                        "symbol": clean_symbol,
                        "name": names.get(symbol, symbol),
                        "price": price,
                        "change": change,
                        "change_pct": change_pct
                    })
            except:
                continue
                
        return results if results else self._get_mock_data()
