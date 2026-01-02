# secure-wireless-firmware-update-esp8266
Secure OTA Firmware Update for ESP8266

This project implements a secure Over-The-Air (OTA) firmware update mechanism for the ESP8266. Firmware is encrypted before transmission, delivered over HTTP, decrypted on the device, verified for integrity, and then flashed safely.

# Objective

To enable the ESP8266 to update firmware wirelessly in a secure and reliable way, without manual USB flashing. The system ensures:
Encrypted firmware transmission
Protection against tampering or modification
Integrity verification before flashing
Safe flashing without corrupting the device

# System Workflow
Arduino IDE → firmware.bin
        ↓
encrypt.py (AES Encryption + SHA256 Hash)
        ↓
Flask Server
  ├── /firmware   → Encrypted firmware
  └── /checksum   → SHA-256 hash
        ↓
ESP8266 OTA Client
  - Download firmware
  - Decrypt using AES-128-CBC
  - Verify checksum
  - Flash to memory
  - Reboot and run update

# Technologies Used

ESP8266 (NodeMCU / Wemos D1 Mini)
Arduino IDE
Python Flask
PyCryptodome
AES-128-CBC Encryption
SHA-256 Hashing
ESP8266 HTTPClient and Update library

# Project Structure
secure-ota-project
 ├── server
 │    ├── app.py           → Flask server
 │    ├── encrypt.py       → Encryption + checksum generator
 │    ├── encrypted.bin    → AES encrypted firmware
 │    └── checksum.txt     → SHA-256 hash
 │
 ├── firmware
 │    ├── firmware_v1.bin
 │    └── firmware_v2.bin
 │
 └── esp
      ├── 1_wifi_test.ino
      ├── 2_checksum_test.ino
      ├── 3_firmware_download_test.ino
      └── 4_secure_ota_final.ino

# Features

Secure AES-128-CBC encrypted firmware delivery
SHA-256 integrity verification
Memory-safe streaming decryption
Reliable OTA flashing
Safe rollback in case of verification failure
Standard HTTP server delivery

# Demonstration Summary

Flask server hosts encrypted firmware and checksum
ESP8266 retrieves checksum and encrypted firmware
Firmware is decrypted block-by-block
Integrity is verified
Firmware is flashed
Device reboots and runs updated firmware

# Challenges and Learnings

Resolved network and firewall access limitations for the server
Managed ESP8266 memory constraints using streamed decryption
Addressed encryption library compatibility and API differences
Achieved a stable OTA update pipeline through staged testing

# Status
Completed and fully functional secure OTA update system for ESP8266.
