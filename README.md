# Portable Text Descriptor For Visually Impaired Users
## Project Overview

An embedded OCR (Optical Character Recognition) application designed to assist visually impaired individuals in reading text from various sources including documents, receipts, restaurant menus, product packages, and instructions. This project demonstrates embedded software engineering principles through real-time image processing, custom algorithm implementation, and hardware-optimized performance.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Development Timeline](#development-timeline)
- [Implementation Platforms](#implementation-platforms)
- [Getting Started](#getting-started)
- [Performance Targets](#performance-targets)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [License](#license)

## Features

### Core Functionality

#### Currently Implemented
- **Real-time camera preview** with CameraX integration
- **Photo capture functionality** with front/back camera switching
- **Modern Android UI** built with Jetpack Compose
- **MVVM architecture** for maintainable code structure
- **Camera permissions handling** for secure access
- **Responsive UI design** with Material Design 3

#### Planned Features
- **OCR text recognition** from captured images
- **Text-to-speech synthesis** for audio output
- **Embedded-optimized algorithms** built from first principles
- **Memory-efficient processing** for resource-constrained devices
- **Cross-platform compatibility** (Android smartphones, embedded devices)

## Architecture
<img width="1480" height="2400" alt="Business process flow example(1)" src="https://github.com/user-attachments/assets/6b97bc7f-6eef-4439-8b52-a13231b89e03" />

## Development Timeline

### Phase 1: Foundation & Research (Weeks 1-3)
**Objectives:** Establish development environment and research baseline
- [X] Literature review on embedded OCR systems
- [X] Platform selection and development environment setup
- [X] Basic camera interface implementation
- [X] Performance benchmarking framework
- [X] Initial project structure and build system

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
- Android Studio Hedgehog | 2023.1.1 or later
- JDK 11 or later
- Android SDK API 24+ (Android 7.0+)
- Gradle 8.11.1+
- Kotlin 2.0.21+

# For Testing
- Android device or emulator with camera
- USB debugging enabled (for physical device testing)
```

### Building the Project

#### Android Build
```bash
# Clone the repository
git clone https://github.com/YutharsanS/Portable-Text-Descriptor.git
cd Portable-Text-Descriptor

# Build the project using Gradle wrapper
./gradlew build

# Build and install debug APK
./gradlew installDebug

# Or open in Android Studio and build from IDE
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
# Run unit tests
./gradlew test

# Run instrumented tests (requires connected device/emulator)
./gradlew connectedAndroidTest

# Run specific test classes
./gradlew test --tests com.example.portabletextdescriptor.ExampleUnitTest
```

## Performance Targets

### Android Application Metrics
- **Camera Preview**: 30 FPS real-time preview
- **Image Capture**: < 500ms from tap to capture
- **UI Responsiveness**: < 16ms frame time for 60 FPS
- **Memory Usage**: < 150MB RAM for optimal performance
- **Battery Life**: Minimal impact during active use
- **Compatibility**: Android 7.0+ (API level 24+)

### Future OCR Performance Goals
- **Text Recognition**: < 2 seconds per image
- **Accuracy**: > 95% for printed text
- **Language Support**: English (primary), expandable
- **File Size**: < 50MB APK size

## Development Workflow

### Current Development Stack
- **Language**: Kotlin
- **UI Framework**: Jetpack Compose
- **Architecture**: MVVM (Model-View-ViewModel)
- **Camera**: CameraX library
- **Build System**: Gradle with Kotlin DSL
- **Version Control**: Git with GitHub

### Development Process
1. **Feature Development**: Create feature branches from `development`
2. **Testing**: Run unit and instrumented tests before commits
3. **Code Review**: Pull requests required for `main` branch
4. **Continuous Integration**: Automated builds and tests
5. **Release**: Tagged releases from `main` branch

### Next Development Phases
- **Phase 3**: OCR Integration (ML Kit or custom implementation)
- **Phase 4**: Text-to-Speech functionality
- **Phase 5**: Performance optimization and accessibility features

## Code Standards

### Kotlin Style Guide
- Follow [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html)
- Use meaningful variable and function names
- Prefer immutable data structures when possible
- Use proper null safety with nullable types

### Android Best Practices
- **Architecture**: MVVM pattern with ViewModels and Compose
- **Dependency Injection**: Prefer constructor injection
- **Resource Management**: Use string resources for user-facing text
- **Accessibility**: Implement content descriptions and screen reader support

### Compose Guidelines
- Use remember for expensive computations
- Prefer stateless composables when possible
- Follow Material Design 3 principles
- Use proper modifier chaining order

### Testing Standards
- Unit tests for ViewModels and business logic
- UI tests for critical user flows
- Minimum 70% code coverage target

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
