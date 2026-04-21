# Communication

> **Manual:** S7-1200 Programmable Controller V20 (11/2024)  
> **Source:** https://docs.tia.siemens.cloud/r/simatic_s7_1200_manual_collection_eses_20/communication  

---

## Table of Contents

- Communication
- Overview
- Secure Vs. Legacy Communication
- Communication Protocols And Ports Used By Ethernet Communication
- Asynchronous Communication Connections
- Supported Certificates
- Profinet
  - Cpu Communication
  - Creating A Network Connection
    - Partner Connection Path
  - Assigning Internet Protocol Ip Addresses
    - Assigning Ip Addresses To Programming And Network Devices
    - Checking The Ip Address And Mac Address Of Your Network Interface
    - Assigning An Ip Address To A Cpu Online
    - Configuring An Ip Address For A Cpu In Your Project
  - Testing The Profinet Network
  - Locating The Ethernet Mac Address On The Cpu
  - Configuring Network Time Protocol Ntp Synchronization
  - Profinet Device Start Up Time Naming And Address Assignment
  - Open User Communication
    - Protocols
    - Tcp And Iso On Tcp
      - Tcp
      - Iso On Tcp
    - Ad Hoc Mode
    - Communication Services And Used Port Numbers
    - Connection Ids For The Open User Communication Instructions
    - Parameters For The Profinet Connection
    - Supported Tls Versions
    - Configuring Dns
    - Configuring An Ouc Connection In The Tia Portal
    - Tsend C And Trcv C Instructions
      - Overview
      - Tsend C And Trcv C Send And Receive Data Using Ethernet
    - Legacy Tsend C And Trcv C Instructions
      - Overview
      - Legacy Tsend C And Trcv C Send And Receive Data Using Ethernet
    - Tcon Tdiscon Tsend And Trcv Instructions
      - Overview
      - Tcon Tdiscon Tsend And Trcv Tcp Communication Instructions
    - Tconsettings
      - Overview
      - Request A Connection Id And If Necessary Specify A Connection Property
      - Reading A Property Of A Prepared Or An Existing Connection
      - Specifying A Property Of A Prepared Or An Existing Connection
      - Which Connection Properties Can Be Read Or Specified
      - Terminating A Tcp Connection
    - Legacy Tcon Tdiscon Tsend And Trcv Instructions
      - Overview
      - Legacy Tcon Tdiscon Tsend And Trcv Tcp Communication Instructions
    - T Reset Terminate And Re Establish An Existing Connection Instruction
    - T Diag Checks The Status Of Connection And Reads Information Instruction
    - Tmail C Send An Email Using The Ethernet Interface Of The Cpu Instruction
      - Overview
      - Mail Addr Param Parameter
      - To S And Cc Parameters
      - Done Busy And Error Parameters
      - Sending Data Logs Recipes And User Files Using Email Attachments
      - Error Condition Codes
        - Status Parameter
        - Sfb Status Parameter Of The Instance Db
    - Udp
    - Tusend And Turcv
      - Tusend And Turcv Udp Communication Instructions
      - Tusend And Turcv Operations
    - T Config
      - T Config Configure Interface Instruction
      - Conf Data Data Block
      - Example Using The T Config Instruction To Change Ip Parameters
      - Example Using The T Config Instruction To Change Ip Parameters And Profinet Io Device Names
      - Example Using The T Config Instruction To Change Ip Addresses In The Ntp Servers
    - Common Parameters For Instructions
    - Restricted Tsaps Or Port Numbers For Passive Iso And Tcp Communication
  - Communication With A Programming Device
    - Overview
    - Establishing The Hardware Communications Connection
    - Configuring The Devices
    - Assigning Internet Protocol Ip Addresses
    - Testing Your Profinet Network
  - Hmi To Plc Communication
    - Overview
    - Configuring Logical Network Connections Between Two Devices
  - Plc To Plc Communication
    - Overview
    - Configuring Logical Network Connections Between Two Devices
      - Partner Connection Path Between Two Devices
    - Configuring Transmit Send And Receive Parameters
      - Configuring Transmit Send And Receive Parameters
      - Configuring The Tsend C Instruction Transmit Send Parameters
      - Configuring The Trcv C Instruction Receive Parameters
  - Configuring A Cpu And Profinet Io Device
    - Adding A Profinet Io Device
    - Assigning Cpus And Device Names
    - Assigning Internet Protocol Ip Addresses
    - Configuring The Io Cycle Time
  - Configuring A Cpu And Profinet I Device
    - I Device Functionality
    - Properties And Advantages Of The I Device
    - Characteristics Of An I Device
    - Data Exchange Between Higher And Lower Level Io System
    - Configuring The I Device
  - Shared Devices
    - Shared Device Functionality
    - Example Configuring A Shared Device Gsd Configuration
    - Example Configuring An I Device As A Shared Device
  - Media Redundancy Protocol Mrp
    - Overview
    - Media Redundancy With Ring Topologies
    - Using Media Redundancy Protocol Mrp
    - Configuring Media Redundancy
  - S7 Routing

---

## Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Secure Vs. Legacy Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Communication Protocols And Ports Used By Ethernet Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Asynchronous Communication Connections

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Supported Certificates

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Profinet

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Cpu Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Creating A Network Connection

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Partner Connection Path

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Assigning Internet Protocol Ip Addresses

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Assigning Ip Addresses To Programming And Network Devices

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Checking The Ip Address And Mac Address Of Your Network Interface

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Assigning An Ip Address To A Cpu Online

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring An Ip Address For A Cpu In Your Project

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Testing The Profinet Network

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Locating The Ethernet Mac Address On The Cpu

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Configuring Network Time Protocol Ntp Synchronization

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Profinet Device Start Up Time Naming And Address Assignment

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Open User Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Protocols

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Tcp And Iso On Tcp

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Tcp

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Iso On Tcp

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Ad Hoc Mode

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Communication Services And Used Port Numbers

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Connection Ids For The Open User Communication Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Parameters For The Profinet Connection

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Supported Tls Versions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring Dns

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring An Ouc Connection In The Tia Portal

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Tsend C And Trcv C Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Tsend C And Trcv C Send And Receive Data Using Ethernet

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Legacy Tsend C And Trcv C Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Legacy Tsend C And Trcv C Send And Receive Data Using Ethernet

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Tcon Tdiscon Tsend And Trcv Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Tcon Tdiscon Tsend And Trcv Tcp Communication Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Tconsettings

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Request A Connection Id And If Necessary Specify A Connection Property

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Reading A Property Of A Prepared Or An Existing Connection

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Specifying A Property Of A Prepared Or An Existing Connection

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Which Connection Properties Can Be Read Or Specified

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Terminating A Tcp Connection

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Legacy Tcon Tdiscon Tsend And Trcv Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Legacy Tcon Tdiscon Tsend And Trcv Tcp Communication Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### T Reset Terminate And Re Establish An Existing Connection Instruction

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### T Diag Checks The Status Of Connection And Reads Information Instruction

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Tmail C Send An Email Using The Ethernet Interface Of The Cpu Instruction

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Mail Addr Param Parameter

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### To S And Cc Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Done Busy And Error Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Sending Data Logs Recipes And User Files Using Email Attachments

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Error Condition Codes

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Status Parameter

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Sfb Status Parameter Of The Instance Db

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Udp

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Tusend And Turcv

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Tusend And Turcv Udp Communication Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Tusend And Turcv Operations

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### T Config

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### T Config Configure Interface Instruction

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Conf Data Data Block

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Example Using The T Config Instruction To Change Ip Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Example Using The T Config Instruction To Change Ip Parameters And Profinet Io Device Names

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Example Using The T Config Instruction To Change Ip Addresses In The Ntp Servers

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Common Parameters For Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Restricted Tsaps Or Port Numbers For Passive Iso And Tcp Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Communication With A Programming Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Establishing The Hardware Communications Connection

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring The Devices

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Assigning Internet Protocol Ip Addresses

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Testing Your Profinet Network

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Hmi To Plc Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring Logical Network Connections Between Two Devices

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Plc To Plc Communication

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring Logical Network Connections Between Two Devices

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Partner Connection Path Between Two Devices

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring Transmit Send And Receive Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Configuring Transmit Send And Receive Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Configuring The Tsend C Instruction Transmit Send Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Configuring The Trcv C Instruction Receive Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Configuring A Cpu And Profinet Io Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Adding A Profinet Io Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Assigning Cpus And Device Names

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Assigning Internet Protocol Ip Addresses

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring The Io Cycle Time

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Configuring A Cpu And Profinet I Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### I Device Functionality

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Properties And Advantages Of The I Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Characteristics Of An I Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Data Exchange Between Higher And Lower Level Io System

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring The I Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Shared Devices

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Shared Device Functionality

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Example Configuring A Shared Device Gsd Configuration

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Example Configuring An I Device As A Shared Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Media Redundancy Protocol Mrp

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Media Redundancy With Ring Topologies

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Using Media Redundancy Protocol Mrp

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Configuring Media Redundancy

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### S7 Routing

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

