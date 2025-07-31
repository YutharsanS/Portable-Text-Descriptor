# Portable Text Descriptor For Visually Impaired Users
## Project Overview

An embedded OCR (Optical Character Recognition) application designed to assist visually impaired individuals in reading text from various sources including documents, receipts, restaurant menus, product packages, and instructions. This project demonstrates embedded software engineering principles through real-time image processing, custom algorithm implementation, and hardware-optimized performance.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Development Timeline](#development-timeline)
- [Implementation Platforms](#implementation-platforms)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Performance Targets](#performance-targets)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [License](#license)

## Features

### Core Functionality
- **Real-time OCR processing** from camera input
- **Text-to-speech synthesis** for audio output
- **Embedded-optimized algorithms** built from first principles
- **Memory-efficient processing** for resource-constrained devices
- ***Cross-platform compatibility** (Android smartphones, embedded devices)

## Architecture
<img width="1480" height="2400" alt="Business process flow example(1)" src="https://github.com/user-attachments/assets/6b97bc7f-6eef-4439-8b52-a13231b89e03" />

## Development Timeline

### Phase 1: Foundation & Research (Weeks 1-3)
**Objectives:** Establish development environment and research baseline
- [X] Literature review on embedded OCR systems
- [X] Platform selection and development environment setup
- [ ] Basic camera interface implementation
- [ ] Performance benchmarking framework
- [ ] Initial project structure and build system

**Deliverables:**
- Development environment documentation
- Baseline performance measurements
- Project architecture specification

## Implementation Platforms
### Primary Platform: Android Smartphone
Target Specifications:
  - ARM based processor
  - Minimum 4GB RAM
  - Android 7.0+
  - Camera with autofocus
  - Audio output capability

## Getting Started

### Prerequisites
```bash
# Android Development
- Android Studio 
- ARM toolchain

# MaixCAM Development (Optional)
- MaixPy/MaixCDK SDK
- RISC-V toolchain
- Linux development environment
```

### Building the Project

#### Android Build
```bash
# yet to be decided
```

#### MaixCAM Build (Optional)
```bash
# Setup MaixPy environment
pip install maixpy
cd embedtext/maixcam
python deploy.py --target maixcam
```

### Running Tests
```bash
# yet to be decided
```

## Project Structure
```
# yet to be decided
```

## Performance Targets

## Development Workflow

## Code Standards

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
