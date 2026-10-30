# Lay Complain SL (Sierra Leone Complaint System)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Architecture](https://img.shields.io/badge/Architecture-Object--Oriented-green.svg)](#architecture--design-patterns)

**Lay Complain SL** is an Object-Oriented Command Line Interface (CLI) application built in Python designed to streamline municipal and civic complaint registration and administrative lifecycle management in Sierra Leone. By linking complaints to National Identification Numbers (NIN), the system ensures identity verification, centralized oversight, and auditability.

---

## Table of Contents
- [Architecture & Design Patterns](#-architecture--design-patterns)
- [System Requirements](#-system-requirements)
- [Installation & Setup](#-installation--setup)
- [Domain Model & API Reference](#-domain-model--api-reference)
  - [Account Module (`app/account/index.py`)](#account-module-appaccountindexpy)
  - [Admin Module (`app/admin/index.py`)](#admin-module-appadminindexpy)
  - [Complainant Module (`app/complinant/index.py`)](#complainant-module-appcomplinantindexpy)
  - [CLI Engine (`app/setup/index.py`)](#cli-engine-appsetupindexpy)
- [Data Storage Schema](#-data-storage-schema)
- [Security & Architectural Audit](#-security--architectural-audit)
- [License](#-license)

---

## Architecture & Design Patterns

The project follows a **Modular Layered Architecture** separating the core entity logic, datastores, and interface execution.

```text
               ┌──────────────────────────────┐
               │    Entry Point (main.py)     │
               └──────────────┬───────────────┘
                              │
               ┌──────────────▼───────────────┐
               │  Orchestrator (Setup Class)  │
               └──────────────┬───────────────┘
                              │
      ┌───────────────────────┼───────────────────────┐
      │                       │                       │
┌─────▼──────────┐    ┌───────▼────────┐    ┌─────────▼─────────┐
│ Account Module │    │  Admin Module  │    │ Complainant Mod.  │
└─────┬──────────┘    └───────┬────────┘    └─────────┬─────────┘
      │                       │                       │
      └───────────────────────┼───────────────────────┘
                              │
               ┌──────────────▼───────────────┐
               │  In-Memory Datastores (Data) │
               └──────────────────────────────┘
```

### Core Patterns Applied:
* **Facade / Controller Pattern**: `Setup.exec()` encapsulates the orchestration of sign-in, authentication checks, role resolution, and input loop lifecycle.
* **Domain Entity Separation**: Clean segregation between user credentials handling (`Account`), platform administration (`Admin`), and user complaints lifecycle (`Complaint`).
* **In-Memory Mock Persistence**: Simulates persistent database interaction using structured Python dictionary objects (`data/users.py` and `data/complaints.py`).

---

## System Requirements

* **Runtime**: Python `3.8` or higher.
* **Dependencies**: Standard Library only (`sys`, `os`, basic I/O). No external third-party dependencies (`pip`) required.

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-organization/lay-complain-sl.git
   cd lay-complain-sl
   ```

2. **Verify directory layout**:
   Ensure your local directory structure matches the required package hierarchy:
   ```text
   lay-complain-sl/
   ├── app/
   │   ├── account/
   │   │   └── index.py
   │   ├── admin/
   │   │   └── index.py
   │   ├── complinant/
   │   │   └── index.py
   │   ├── data/
   │   │   ├── complaints.py
   │   │   └── users.py
   │   ├── setup/
   │   │   └── index.py
   │   └── main.py
   └── LICENSE.md
   ```

3. **Launch the application**:
   Run the entry script from the repository root:
   ```bash
   python3 app/main.py
   ```

---

## Domain Model & API Reference

### Account Module (`app/account/index.py`)
Encapsulates user authentication, credentials validation, and registration logic.

#### Class: `Account`
* **`__init__(email: str, password: str, NIN: str, username: str)`**: Initializes account context.
* **`sign_up() -> None`**: Appends the current object instance data as a dict to the global `users` store.
* **`sign_in() -> str`**: Validates `email` and `password` against `users`. Returns `'OK'` on success, prints an error and returns `''` on failure.

---

### Admin Module (`app/admin/index.py`)
Provides elevated capabilities for system oversight and complaint maintenance.

#### Class: `Admin`
* **`view_all_complaints() -> None`**: Iterates through all registered complaints in `complaints` and renders non-empty complaints to standard output.
* **`remove_complaint(NIN: str) -> str`**: Locates and removes a complaint matching the target `NIN`. Returns `'OK'` on success or `'NOT FOUND'` on index lookup failure.

---

### Complainant Module (`app/complinant/index.py`)
Manages single-user complaint interaction linked via National Identification Number (`NIN`).

#### Class: `Complaint`
* **`__init__(NIN: str)`**: Binds instance to a target `NIN`.
* **`add_complaint(complaint: str) -> None`**: Creates and attaches a complaint dictionary to global storage.
* **`update_complaint(complaint: str) -> None`**: Searches global state by `NIN` and mutates the existing complaint string.
* **`view_complaint() -> None`**: Fetches and renders the complaint matching the user's `NIN`.

---

### CLI Engine (`app/setup/index.py`)

#### Class: `Setup`
* **`exec() [classmethod] -> None`**: Entry execution block managing interactive CLI loops, input evaluation, and state transition between administrative and standard complainant menus.

---

## Data Storage Schema

### Pre-seeded Users (`app/data/users.py`)

| Field | Type | Description |
| :--- | :--- | :--- |
| `NIN` | `str` | National Identification Number (Primary Key reference) |
| `email` | `str` | User login email address |
| `username` | `str` | Handle / Display Name |
| `password` | `str` | Plaintext password store (Demo purposes) |
| `role` | `str` | Access control tier (`"admin"` or `""` for regular user) |

```python
# System User Seed Data
users = [
    {
        "NIN": "1RT51H", 
        "email": "danner@gmail.com", 
        "username": "danner", 
        "password": "danner123", 
        "role": "admin"
    },
    {
        "NIN": "7YI88Q", 
        "email": "lagga@gmail.com", 
        "username": "lagga", 
        "password": "lagga456", 
        "role": ""
    }
]
```

---

## Security & Architectural Audit

While functional as a prototype, the code exhibits specific operational edge cases to address in production iterations:

1. **In-Memory Storage volatile lifecycle**: Data changes are lost once process execution terminates. Integrate standard storage adapters (`sqlite3`, PostgreSQL, or JSON serialization).
2. **Plaintext Passwords**: Password fields in `users.py` are unhashed. Production environments should utilize secure salted hashing (`bcrypt` or `argon2`).
3. **List Index Edge Cases**: 
   * `list.index()` calls raise `ValueError` if the value is missing. 
   * Checking `if self.index:` treats index `0` as falsy (`False`), leading to misrouted control flows for the first array element.

---

## License

This software is licensed under the **MIT License**. For complete copyright and permission terms, review the [LICENSE.md](LICENSE.md) file.