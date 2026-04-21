# Extended Instructions

> **Manual:** S7-1200 Programmable Controller V20 (11/2024)  
> **Source:** https://docs.tia.siemens.cloud/r/simatic_s7_1200_manual_collection_eses_20/extended-instructions  

---

## Table of Contents

- Extended Instructions
- Date Time Of Day And Clock Functions
  - Date And Time Of Day Instructions
  - Clock Functions
  - Set Timezone Set Timezone
  - Rtm Runtime Meters
- String And Character
  - String Data Overview
  - S Move Move Character String
  - String Conversion Instructions
      - From Character String And Number Instructions
      - From Character String And Array Of Char Instructions
      - From Ascii String And Hexadecimal Number Instructions
  - String Operation Instructions
    - Max Len Maximum Length Of A Character String
    - Len Determine The Length Of A Character String
    - Concat Combine Character Strings
    - Left Right And Mid Read Substrings In A Character String Instructions
    - Delete Delete Characters In A Character String
    - Insert Insert Characters In A Character String
    - Replace Replace Characters In A Character String
    - Find Find Characters In A Character String
  - Runtime Information
    - Getsymbolname Read Out A Tag On The Input Parameter
    - Getsymbolpath Query Composite Global Name Of The Input Parameter Assignment
    - Getinstancename Read Out Name Of The Block Instance
    - Getinstancepath Query Composite Global Name Of The Block Instance
    - Getblockname Read Out Name Of The Block
  - O Profinet Profibus Or As I
      - Write Data Record
    - Getio Read Process Image
    - Setio Transfer Process Image
    - Getio Part Read Process Image Area
    - Setio Part Transfer Process Image Area
    - Ralrm Receive Interrupt
      - Disable Profinet Io Devices
    - Status Parameter For Rdrec Wrrec And Ralrm
    - Others
        - Write Consistent Data
      - Rcvrec Receive Data Record
      - Prvrec Make Data Record Available
      - Dpnrm Dg Read Diagnostic Data From A Profibus Dp Slave
- Profienergy
- Interrupts
    - Detach An Ob And An Interrupt Event Instructions
  - Cyclic Interrupts
    - Set Cint Set Cyclic Interrupt Parameters
    - Qry Cint Query Cyclic Interrupt Parameters
  - Time Of Day Interrupts
    - Ntp Security Overview
    - Set Tintl Set Time Of Day Interrupt
    - Can Tint Cancel Time Of Day Interrupt
    - Act Tint Activate Time Of Day Interrupt
    - Qry Tint Query Status Of Time Of Day Interrupt
  - Time Delay Interrupts
    - Enable Execution Of Higher Priority Interrupts And Asynchronous Error Events Instructions
- Alarms
  - Gen Usrmsg Generate User Diagnostic Alarms
- Diagnostics Profinet Or Profibus
  - Rd Sinfo Read Current Ob Start Information
  - Led Read Led Status
  - Get Im Data Read The Identification And Maintenance Data
  - Get Name Read The Name Of A Profinet Io Device
  - Getstationinfo Read The Ip Or Mac Address Of A Profinet Io Device
  - Devicestates Instruction
      - O System
    - Devicestates Example Configurations
  - Modulestates Instruction
    - Modulestates Read Module Status Information Of A Module
    - Modulestates Example Configurations
  - Get Diag Read Diagnostic Information
  - Getsmcinfo Reading Out Information About The Memory Card
- Pulse
  - Ctrl Pwm Pulse Width Modulation
  - Ctrl Pto Pulse Train Output
  - Operation Of The Pulse Outputs
  - Configuring A Pulse Channel For Pwm Or Pto
- Recipes And Data Logs
  - Recipes
    - Recipe Overview
    - Recipe Example
    - Program Instructions That Transfer Recipe Data
      - Recipeexport Recipe Export
      - Recipeimport Recipe Import
    - Recipe Example Program
  - Data Logs
    - Data Log Overview
    - Data Log Record Structure
    - Program Instructions That Control Data Logs
      - Datalogcreate Create Data Log
      - Datalogopen Open Data Log
      - Datalogwrite Write Data Log
      - Datalogclear Empty Data Log
      - Datalogclose Close Data Log
      - Datalogdelete Delete Data Log
      - Datalognewfile Data Log In New File
    - Working With Data Logs
    - Limit To The Size Of Data Log Files
    - Data Log Example Program
- Data Block Control
  - Create Db Create Data Block
    - Write A Data Block In Load Memory Instructions
  - Attr Db Read Data Block Attribute
  - Delete Db Delete Data Block
- Address Handling
  - Geo2log Determine The Hardware Identifier From The Slot
  - Log2geo Determine The Slot From The Hardware Identifier
    - O Address
  - Rd Addr Determine The Io Addresses From The Hardware Identifier
  - Geoaddr System Data Type
- Common Error Codes For The Extended Instructions
- File Handling
  - Filereadc Read File From The Memory Card
  - Filewritec Write File On The Memory Card
  - Filedelete Delete File On The Memory Card

---

## Extended Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Date Time Of Day And Clock Functions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Date And Time Of Day Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Clock Functions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Set Timezone Set Timezone

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Rtm Runtime Meters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## String And Character

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### String Data Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### S Move Move Character String

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### String Conversion Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### From Character String And Number Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### From Character String And Array Of Char Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### From Ascii String And Hexadecimal Number Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### String Operation Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Max Len Maximum Length Of A Character String

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Len Determine The Length Of A Character String

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Concat Combine Character Strings

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Left Right And Mid Read Substrings In A Character String Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Delete Delete Characters In A Character String

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Insert Insert Characters In A Character String

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Replace Replace Characters In A Character String

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Find Find Characters In A Character String

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Runtime Information

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Getsymbolname Read Out A Tag On The Input Parameter

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Getsymbolpath Query Composite Global Name Of The Input Parameter Assignment

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Getinstancename Read Out Name Of The Block Instance

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Getinstancepath Query Composite Global Name Of The Block Instance

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Getblockname Read Out Name Of The Block

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### O Profinet Profibus Or As I

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Write Data Record

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Getio Read Process Image

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Setio Transfer Process Image

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Getio Part Read Process Image Area

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Setio Part Transfer Process Image Area

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Ralrm Receive Interrupt

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Disable Profinet Io Devices

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Status Parameter For Rdrec Wrrec And Ralrm

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Others

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Write Consistent Data

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Rcvrec Receive Data Record

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Prvrec Make Data Record Available

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Dpnrm Dg Read Diagnostic Data From A Profibus Dp Slave

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Profienergy

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Interrupts

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Detach An Ob And An Interrupt Event Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Cyclic Interrupts

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Set Cint Set Cyclic Interrupt Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Qry Cint Query Cyclic Interrupt Parameters

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Time Of Day Interrupts

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Ntp Security Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Set Tintl Set Time Of Day Interrupt

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Can Tint Cancel Time Of Day Interrupt

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Act Tint Activate Time Of Day Interrupt

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Qry Tint Query Status Of Time Of Day Interrupt

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Time Delay Interrupts

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Enable Execution Of Higher Priority Interrupts And Asynchronous Error Events Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Alarms

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Gen Usrmsg Generate User Diagnostic Alarms

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Diagnostics Profinet Or Profibus

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Rd Sinfo Read Current Ob Start Information

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Led Read Led Status

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Get Im Data Read The Identification And Maintenance Data

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Get Name Read The Name Of A Profinet Io Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Getstationinfo Read The Ip Or Mac Address Of A Profinet Io Device

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Devicestates Instruction

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### O System

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Devicestates Example Configurations

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Modulestates Instruction

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Modulestates Read Module Status Information Of A Module

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Modulestates Example Configurations

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Get Diag Read Diagnostic Information

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Getsmcinfo Reading Out Information About The Memory Card

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Pulse

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Ctrl Pwm Pulse Width Modulation

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Ctrl Pto Pulse Train Output

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Operation Of The Pulse Outputs

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Configuring A Pulse Channel For Pwm Or Pto

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Recipes And Data Logs

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Recipes

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Recipe Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Recipe Example

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Program Instructions That Transfer Recipe Data

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Recipeexport Recipe Export

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Recipeimport Recipe Import

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Recipe Example Program

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Data Logs

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Data Log Overview

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Data Log Record Structure

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Program Instructions That Control Data Logs

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Datalogcreate Create Data Log

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Datalogopen Open Data Log

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Datalogwrite Write Data Log

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Datalogclear Empty Data Log

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Datalogclose Close Data Log

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Datalogdelete Delete Data Log

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

##### Datalognewfile Data Log In New File

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Working With Data Logs

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Limit To The Size Of Data Log Files

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Data Log Example Program

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Data Block Control

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Create Db Create Data Block

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### Write A Data Block In Load Memory Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Attr Db Read Data Block Attribute

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Delete Db Delete Data Block

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Address Handling

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Geo2log Determine The Hardware Identifier From The Slot

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Log2geo Determine The Slot From The Hardware Identifier

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

#### O Address

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Rd Addr Determine The Io Addresses From The Hardware Identifier

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Geoaddr System Data Type

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## Common Error Codes For The Extended Instructions

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

## File Handling

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Filereadc Read File From The Memory Card

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Filewritec Write File On The Memory Card

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

### Filedelete Delete File On The Memory Card

Loading application...

Your web browser must have JavaScript enabled in order for this application to display correctly.

---

