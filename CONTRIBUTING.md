# Contributing to MCP Server

We welcome contributions to the MCP Server project! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/mcp-server.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Install dev dependencies: `pip install pytest pytest-cov black isort flake8`

## Development Workflow

1. Create a new branch for your feature: `git checkout -b feature-name`
2. Make your changes
3. Run tests: `pytest`
4. Format your code: `black src tests` and `isort src tests`
5. Lint your code: `flake8 src tests`
6. Commit your changes: `git commit -m "Add feature description"`
7. Push to your fork: `git push origin feature-name`
8. Create a Pull Request

## Code Style

We follow PEP 8 and use Black for code formatting. Please ensure your code is formatted with Black before submitting a PR.

## Testing

All new features should include tests. We use pytest for testing.

## Documentation

Please update the documentation when adding or modifying features.
