# Web server


---

## Web server overview

The Web server for the S7-1200 provides Web page access to data about your CPU and process data.

|  |  |
| --- | --- |
| You can access the S7-1200 Web pages from a PC or from a mobile device. For devices with small screens, the Web server supports a collection of [basic pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/mlhbK0vfPzNGjGOQTfxulw?section=X9cfbdd5e92998f97ce9002f6b86a1419).  You use a Web browser to access the IP address of the S7‑1200 CPU or the IP address of a [Web server-enabled CP (communications processor) module](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/H8v_ZyWzJV4IpD~luNGAwg?section=X05a9645e263fbf69039c35b0ff635f64) in the local rack with the CPU to establish the connection. The S7‑1200 supports multiple concurrent connections. |  |

Note:

**Web server multiple concurrent connections**

The S7-1200 Web server allows for 30 concurrentconnections (assuming that you have enough dynamic connections). Open browser instances can consume between 2 to 8 connections each. The Web server allows up to 7 logged-in users but Siemens recommends that you keep the number of concurrent users as low as possible. An average of 7 users at a time is typically okay under average workloads.

## Standard Web pages

The S7-1200 includes [standard Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/wYbAoKDX_XQ_9F0P~5rJkg?section=X165292e35124f741a26d2259be560c6f) that you can [access from the Web browser of your PC](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Pk22gvnKDsZai3~SSAUQ8g?section=Xfc685e5b6a11fb2831d7fd61c3885d96) or from a [mobile device](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/JLSeGuLG1fSY0rSd0JHCCw?section=X19bf2a7d91369c5784bdbe4400aed0df):

- [Introduction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829) - entry point to the standard Web pages
- [Start Page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/KpWxn_ktke79JixTh8UAgQ?section=Xbf3d5594d5fef020a4656378d3073627) - general information about the CPU
- [Diagnostics](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/yl7zlClN1FrkcWbdPEPU0w?section=Xb0b8b69aad8bca2cf848e4a08ef54022) - detailed information about the CPU including serial, order, and version numbers, program protection, and memory usage
- [Diagnostics Buffer](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/9kXUDdUj5ShypnMNTjz3Gw?section=X842e9cd18ac6639aaf40d0b148b89d19) - the diagnostics buffer
- [Module Information](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zkw1i6aTf022QhpONsl5wA?section=X9fd7e004bb711f264161b0cf27efe2e5) - information about the local and remote modules and the ability to update firmware for modules
- [Communication](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3CtjZV~994YcPWji5oRs_Q?section=Xed857ed09e014090768e1f60ac08d2af) - information about the network addresses, physical properties of the communication interfaces, statistics, parameters, as well as a connection summary and diagnostic information
- [Tag status](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f7WatsxclQNha2u2VG9y0g?section=X37eac0b13e3c4cc90b9bdcbd15642672) - CPU variables and I/O, accessible by address or PLC tag name
- [Watch tables](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/slqDdcEVd6jLXnTqF9vRPg?section=Xc90b523b21099b5ef9875b12ea0cf151) - watch tables that you configured in STEP 7
- [Online backup](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/isBliVNTXNJ6NCzfBBr7pg?section=X10d08635decfd77ea365a39fc4668fd0) - ability to backup an online CPU or restore a previously-made online backup
- [Data Logs](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/mZZAYWI3qGGsoDurXWiHRQ?section=X99e5f10f7bebfbb0e13313f2836182a3) - ability to view a list of all data logs on the PLC, download a data log from the PLC to your computer, delete a data log from the PLC, and retrieve and clear a data log from the PLC
- [User Files](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/1oN_XWyhd4NVq8KmgLmtGA?section=X1a6c6a1b16f3caba9eb4fe292b939ccf) - ability to view a list of user files on the PLC, download a user file from the PLC to your computer, upload a user file from your computer to the PLC, and delete a user file on your PLC
- [User-defined pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/2KzF92LTmuWCFy~i1g7GCg?section=Xb80e2d2e444f309df8d7543d837f1d4b) - create user-defined Web pages to access CPU data
- [File Browser](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f1bXzgmsxyQgQcYAqC77rA?section=X81170b06653aefc28fb2399202cdb341) - browser for files stored internally in the CPU or on a memory card, for example, data logs and recipes
- [Login](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nDYnYbhrwbHcYZyUn7lygQ?section=Xf14b550dd189216efc1093d424d335ad) - log in as a different user, or log out.

These pages are included in the S7-1200 CPU firmware, and are available in English, German, French, Spanish, Italian, and Simplified Chinese. Additional configuration is needed in TIA Portal to view PLC diagnostic messages (chapter 15). All pages except for the Introduction and Start page require additional [user privileges](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785) that you configure in STEP 7 to view the page.

## User-defined Web pages

The S7-1200 also provides support for you to create user-defined Web pages that can access CPU data. You can develop these pages with the HTML authoring software of your choice, and include pre-defined "AWP" (Automation Web Programming) commands in your HTML code to access CPU data. Refer to the [User-defined Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/uODji4nS8sQYGJMdmQ28dA?section=Xcef07d3d9324c934502e2fbb17e27fbb) chapter for specific information on the development of user-defined Web pages, and the associated configuration and programming in STEP 7.

You can access the user-defined pages from either a PC or mobile device from the standard or basic Web pages. You can also configure one of your user-defined Web pages to be the [entry page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/gkY3~3V~j5L9s3vT2Dqc3w?section=X49d1982058a49937a91d62b575a1c58f) for the Web server.

## Web API

The S7‑1200 CPU also provides a [Web API](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/YHTsNZvUGlhqWEvVg7fHOg?section=Xbf88af32d0701fbad1d76e8d02c39527) that is an interface for you to read and write process data.

## Web browser requirement

Siemens has tested the Web server standard pages and verifies support of the following Web browsers:

- Microsoft Edge V116.0
- Mozilla Firefox V116.0.3
- Opera V102.0
- Google Chrome V116.0
- Android browser V7.x, 8.x, 10.x, 11.x, and 12.x
- Mobile Chrome for Android V7.x, 8.x, 10.x, 11.x, and 12.x
- Mobile Safari and Chrome for iOS V12.5.1 and V16.5

When using the HTML Browser control in a WinCC project, the Web server supports the following Siemens HMI Panels for the standard pages:

- Basic Panels

  - Gen 2 KTP400 to KTP1200
- Comfort Panels

  - TP700 to TP2200
  - KP400 to KP1500
  - KTP400
  - TP700 Comfort Outdoor
- Mobile Panels

  - Gen 2 KTP700[F], KTP900[F]
- Unified Comfort Panels

  - Basic Panel (2nd Gen)
  - Mobile Panel (2nd Gen)

For browser-related restrictions that can interfere with the display of standard or user-defined Web pages, see the [Constraints](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/JVfjZHIUv4d~PmKXSo_~PQ?section=X9dae4d63cb6bd00efe5f7c06aab9ecb8) section.

## Web server performance

Many factors can affect the performance of the Web server. The S7-1200 CPU and the programming device must share time with other tasks that consume resources and processing time. If you have poor performance with the Web server, try these adjustments to improve Web server performance:

- Increase the [communication load](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/bbPOB2tX2nZmvJCQLRHIQw?section=X65fdb12a60f84cc807327a8f234890c4) on the PLC from 20% to 50%.
- Configure a [minimum scan time](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/OsRe4QwxuGBGsAZXbyVOmQ?section=Xbac149a33424f66ef5397f5ee9947be8). Setting a minimum scan time provides increased communication time between the S7-1200 CPU and the programming device.
- Increase the "Update interval" time in TIA Portal from the default 10s.
- Use the S7-1200 CPU's Ethernet interface instead of a [CP module](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/H8v_ZyWzJV4IpD~luNGAwg?section=X05a9645e263fbf69039c35b0ff635f64) to access the Web server.

---

## Enabling the Web server

You enable the Web server in STEP 7 from Device Configuration for the CPU to which you intend to connect.

To enable the Web server, follow these steps:

1. Select the CPU in the Device Configuration view.
2. In the inspector window, select "Web server" from the CPU properties.
3. Select the check box for "Activate web server on all modules of this device".
4. For increased security, ensure that "Permit access only with HTTPS" is selected to require secure access to the Web server over [TLS](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/5YWlWuw4QgpJV1CzwrG8pw?section=X50092ac4ea18888e4a9d61ce3e65ca66). To use HTTPS for secure communication, you must configure a Web server certificate. Configure Web server certificates from Device configuration for the CPU. From the CPU properties, select Web server > Security to configure [Web server certificates](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/0HuKkB3PdN5AHLWA2Zf0Zw?section=Xadd2fa9c957dbb69c387358bec35ae05).
5. If you select "Enable automatic update" for "Automatic update", standard Web pages will refresh by default every ten seconds. You can also enter a custom refresh time period in seconds for the "Update interval" field.
6. Depending upon the type of interface access used, you must ensure that Web server access is enabled for that interface:

   - PLC PROFINET: Ensure that the "Enable Web server for the IP address of this interface" property is enabled on the PLC for the Web server to be accessible through the PLC PROFINET interface.
   - WanCP PROFINET port: If you are using a WanCP device, ensure that the property "Enable Web server for the IP address of this interface" property is checked in order to have the Web server accessible through the particular WanCP PROFINET port.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/k3ThCWSe1GW6kQqRjibiJw-VBkTPlmjVZAl17lebjV9hA/content?v=3390426a5b111e4b)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/k3ThCWSe1GW6kQqRjibiJw-VBkTPlmjVZAl17lebjV9hA)

Warning:

**Unauthorized access to a CPU**

Users with CPU full access or full access (incl. fail-safe) privileges have privileges to read and write PLC variables. Regardless of the access level for the CPU, Web server or OPC UA users can have privileges to modify PLC data and execute functions. Unauthorized access to the CPU can disrupt process operation.

Siemens recommends that you observe the following security practices:

- Enable [Access control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7nIuqWCd4bYr85ym87r3Cg?section=Xacdebbc7e299aa37867bfd6f048080e1) under "Protection & Security > Access control".
- Do not enable the "Anonymous" user.
- Use strong passwords, as defined in STEP 7.
- Enable the setting "Only allow secure PG/PC and HMI communication" under "Protection & Security > Connection mechanisms".
- Use a secure Virtual Private Network (VPN) to connect to the S7-1200 PLC from a location outside your protected network.
- Enable access to the Web server only with the HTTPS protocol.
- Perform error-checking and range-checking on your variables in your program logic because Web server or OPC UA users can change PLC variables to invalid values.
- For the OPC UA server: In your STEP 7 Device configuration, navigate to "Properties > OPC UA > Server > Security" and deselect "No security" in "Security policies available on the server for the secure channel".

Disruption of process operations can result in death, severe personal injury, and/or property damage.

After you download the device configuration, you can use the standard Web pages to access the Introduction and Start page of the CPU. To access additional pages, you must configure one or more [Web server users](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785).

If you created and enabled [user-defined Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/uODji4nS8sQYGJMdmQ28dA?section=Xcef07d3d9324c934502e2fbb17e27fbb), you can access them from the standard or basic Web page navigation menu.

Note:

**Device exchange: Replacing a V3.0 CPU with a V4.x CPU**

If you [replace an existing V3.0 CPU with a V4.x CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/sY9a~e7vuNtxkBlyZ2kc_g?section=Xb948e7b5080772e56e2047b01d0b24a1) and convert your V3.0 project to a V4.x project, note that STEP 7 and the V4.x CPU retain the Web server settings for

- "Activate web server on all modules of this device"
- "Permit access only with HTTPS"

Note:

If a ["Download in RUN"](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PPT275Llk_wsnVgNq0TnYg?section=X1a1165b093d3591682068ea01cff3774)  is in progress, standard and user-defined Web pages do not update data values or permit you to write data values until the download is complete. The Web server discards any attempts to write data values while a download is in progress.

---

## Web server user management


---

### Assigning Web server user privileges for V4.7 configured CPUs

If the firmware version of the CPU in your STEP 7 project is V4.7 or later, you can assign user privileges for accessing the CPU through the Web server with [User Management & Access Control (UMAC)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7nIuqWCd4bYr85ym87r3Cg?section=Xacdebbc7e299aa37867bfd6f048080e1).

Assign roles and rights by doing the following:

1. Select "Security Settings" in the STEP 7 project tree.
2. Double-click "Users and roles".

From Users and Roles, you can add a user, create a new role, assign rights to the new role, and assign the role to a user.

To add a user, do the following:

1. Select the "Users" tab on the top, right side of the window.
2. Double-click "add a new user", then select "Add new local user" from the pop-up.
3. Enter the User name and Password. Runtime timeout defaults to 30 minutes but can be configured by entering the time manually in the field or using the arrows to change the time by one minute increments . The UM domain ID and Comment fields are optional.

To create a new role, follow these steps:

1. Select the "Roles" tab from the top, right side of the window.
2. In the "Roles" section, double-click "Add new role".
3. Enter the Role Name, Description, Runtime timeout, and optional Comment.

Assign rights to the role in the following way:

1. Click the "Runtime rights" tab in the bottom window.
2. Select your PLC from the "Runtime rights" dropdown at left. This will populate all of the Function rights you can assign for that PLC.
3. Select the check boxes that you wish to assign for this role.

To assign a role to a user, do the following:

1. Select the "Users" tab on the top, right side of the window.
2. Click the check box and highlight the name of the user you want to assign with a role.
3. Click the "Assigned roles" tab in the bottom window.
4. Select the check box next to the role(s) you want to assign to the user.

After you download the configuration to the CPU, only authorized users can access Web server functions for which they have privileges.

## Web server access levels

The default "Anonymous" user is disabled for security. You can enable the Anonymous user by selecting the checkbox and agreeing to the security warning. For more information on working with the anonymous user, see "Managing users and roles > Activating or deactivating anonymous user" in the TIA Portal Information System.

Assignable user privileges are as follows:

- Read diagnostics
- Change web server default page
- Change operating mode
- Change time settings
- Create a backup of the CPU
- Change parameter of the F-System (F-Admin)1
- Flash LEDs
- Open user-defined web pages
- Update firmware
- Read files
- Read syslog buffer on the CPU
- Read process data
- Read process data of watch tables
- Restore the CPU using a backup file
- Write/delete files
- Write process data
- Write process data via automation webpage programming (AWP) command
- Write process data of watch tables

1 Available for Failsafe CPUs only.

Note that If you have set a [user-defined Web page to be the entry page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/gkY3~3V~j5L9s3vT2Dqc3w?section=X49d1982058a49937a91d62b575a1c58f) for the Web server, the user must have the "Open user-defined web pages" privilege.

See below an example of user roles and rights configured for a Web server user in the STEP 7 project for an S7-1200 V4.7 Failsafe CPU:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/oTZ_BxcAuxAxRt6v_yTI1w-VBkTPlmjVZAl17lebjV9hA/content?v=9c9796660629a7af)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/oTZ_BxcAuxAxRt6v_yTI1w-VBkTPlmjVZAl17lebjV9hA)

Warning:

**Unauthorized access to a CPU**

Users with CPU full access or full access (incl. fail-safe) privileges have privileges to read and write PLC variables. Regardless of the access level for the CPU, Web server or OPC UA users can have privileges to modify PLC data and execute functions. Unauthorized access to the CPU can disrupt process operation.

Siemens recommends that you observe the following security practices:

- Enable [Access control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7nIuqWCd4bYr85ym87r3Cg?section=Xacdebbc7e299aa37867bfd6f048080e1) under "Protection & Security > Access contro.
- Do not enable the "Anonymous" user.
- Use strong passwords, as defined in STEP 7.
- Enable the setting "Only allow secure PG/PC and HMI communication" under "Protection & Security > Connection mechanisms".
- Use a secure Virtual Private Network (VPN) to connect to the S7-1200 PLC from a location outside your protected network.
- Enable access to the Web server only with the HTTPS protocol.
- Perform error-checking and range-checking on your variables in your program logic because Web server or OPC UA users can change PLC variables to invalid values.
- For the OPC UA server: In your STEP 7 Device configuration, navigate to "Properties > OPC UA > Server > Security" and deselect "No security" in "Security policies available on the server for the secure channel".

Disruption of process operations can result in death, severe personal injury, and/or property damage.

Note:

**Update password encryption for device exchange to V4.x**

After a device exchange to V4.x, you must update the Web server user password encryption. From the CPU's device configuration in the TIA Portal, click the "Upgrade password encryption" button in the Web server user management.

---

### Assigning Web server user privileges for CPU project configurations earlier than V4.7

User Management & Access Control (UMAC) is only available when the configured firmware version of the CPU in the project is V4.7 or later.

If you have a CPU configured in your STEP 7 project to use a firmware version earlier than V4.7, you assign Web server users with various privilege levels under "Properties > Web server > User management". Enter user names, access levels, and passwords for the user logins that you want to provide.

After you download the configuration to the CPU, only authorized users can access Web server functions for which they have privileges.

## Web server access levels

STEP 7 provides a default user named "Everybody" with no password. By default, this user has no additional privileges and can only view the [Start](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/KpWxn_ktke79JixTh8UAgQ?section=Xbf3d5594d5fef020a4656378d3073627) and [Introduction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829) standard Web pages. You can, however, configure additional privileges for the "Everybody" user as well as other users:

- Query diagnostics
- Read tags
- Write tags
- Read tag status
- Write tag status
- Open user-defined web pages
- Write in user-defined web pages
- Read files
- Write/delete files
- Change operating mode
- Flash LEDs
- Perform a firmware update
- Backup CPU
- Restore CPU
- Change system parameter
- Change application parameter

If you have set a [user-defined Web page to be the entry page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/gkY3~3V~j5L9s3vT2Dqc3w?section=X49d1982058a49937a91d62b575a1c58f) for the Web server, the Everybody user must have the "Open user-defined web pages" privilege.

Warning:

**Unauthorized access to a CPU**

Users with CPU full access or full access (incl. fail-safe) privileges have privileges to read and write PLC variables. Regardless of the access level for the CPU, Web server or OPC UA users can have privileges to modify PLC data and execute functions. Unauthorized access to the CPU can disrupt process operation.

Siemens recommends that you observe the following security practices:

- Enable [Access control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7nIuqWCd4bYr85ym87r3Cg?section=Xacdebbc7e299aa37867bfd6f048080e1) under "Protection & Security > Access control".
- Do not enable the "Anonymous" user.
- Use strong passwords, as defined in STEP 7.
- Enable the setting "Only allow secure PG/PC and HMI communication" under "Protection & Security > Connection mechanisms".
- Use a secure Virtual Private Network (VPN) to connect to the S7-1200 PLC from a location outside your protected network.
- Enable access to the Web server only with the HTTPS protocol.
- Perform error-checking and range-checking on your variables in your program logic because Web server or OPC UA users can change PLC variables to invalid values.
- For the OPC UA server: In your STEP 7 Device configuration, navigate to "Properties > OPC UA > Server > Security" and deselect "No security" in "Security policies available on the server for the secure channel".

Disruption of process operations can result in death, severe personal injury, and/or property damage.

Note:

**Update password encryption for device exchange to V4.x**

After a [device exchange](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/sY9a~e7vuNtxkBlyZ2kc_g?section=Xb948e7b5080772e56e2047b01d0b24a1) to V4.x, you must update the Web server user password encryption. From the CPU's device configuration in the TIA Portal, click the "Upgrade password encryption" button in the Web server user management.

---

### User configuration compatibility

## Upgrading configured firmware from an earlier version to V4.7

When you upgrade the configured firmware version in your STEP 7 project to V4.7, STEP 7 migrates users that you previously configured in "User management" to "Users and Roles". You reassign user passwords in the Project tree under "Security settings > Users and roles > Users."

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/QSY9~9_1TVwXdiZDi6t8oA-VBkTPlmjVZAl17lebjV9hA/content?v=218d4336d35f08c4)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/QSY9~9_1TVwXdiZDi6t8oA-VBkTPlmjVZAl17lebjV9hA)

For more information about Web server user privileges when upgrading firmware in the STEP 7 project, see "Editing devices and networks > Configuring devices and networks > Creating configurations > Configuring automation systems > Functional description of S7-1200 CPUs > Setting the operating behavior > Protection and Security > Settings for users and roles > Information about compatibility" in the TIA Portal Information System.

## Downgrading configured firmware from V4.7 to an earlier version

When you downgrade the configured firmware version in your STEP 7 project from V4.7 to an earlier version, users configured in the Project tree under "Security settings > Users and roles > Users" will not be migrated. Users must be reconfigured in device "Properties > User management".

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/ibd_lrw_9LzFK5er1OqaQA-VBkTPlmjVZAl17lebjV9hA/content?v=f9c8955e421748b2)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ibd_lrw_9LzFK5er1OqaQA-VBkTPlmjVZAl17lebjV9hA)

For more information about Web server user privileges when downgrading firmware in the STEP 7 project, see "Editing devices and networks > Configuring devices and networks > Creating configurations > Configuring automation systems > Functional description of S7-1200 CPUs > Setting the operating behavior > Protection and Security > Settings for users and roles > Information about compatibility" in the TIA Portal Information System.

---

## Accessing the Web pages from a PC

You can access the S7-1200 standard Web pages from a PC or from a mobile device through the IP address of the S7‑1200 CPU or the IP address of any [Web server-enabled CP](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/H8v_ZyWzJV4IpD~luNGAwg?section=X05a9645e263fbf69039c35b0ff635f64) in the local rack.

To access the S7-1200 standard Web pages from a PC, follow these steps:

1. Ensure that the S7-1200 and the PC are on a common Ethernet network or are connected directly to each other with a standard Ethernet cable.
2. Open a Web browser and enter the URL "https://ww.xx.yy.zz", where "ww.xx.yy.zz" corresponds to the IP address of the S7-1200 CPU or the IP address of a CP in the local rack.

The Web browser opens the [Introduction standard Web page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829) or the Default HTML page of your user-defined Web pages if you configured it to be the [entry page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/gkY3~3V~j5L9s3vT2Dqc3w?section=X49d1982058a49937a91d62b575a1c58f).

Note:

Use a secure Virtual Private Network (VPN) to connect to the S7-1200 PLC Web server from a location outside your protected network. Be aware also of any [constraints](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/JVfjZHIUv4d~PmKXSo_~PQ?section=X9dae4d63cb6bd00efe5f7c06aab9ecb8) that your Web environment or operating system might impose.

## Accessing standard Web pages by entering the page URL

You can access a specific standard Web page from the URL of the page. To do so, enter the URL in the form "https://ww.xx.yy.zz/<page>.html", where "ww.xx.yy.zz" corresponds to the IP address of the S7-1200 CPU or the IP address of a CP in the local rack:

- https://ww.xx.yy.zz/login.html - page to [log in](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nDYnYbhrwbHcYZyUn7lygQ?section=Xf14b550dd189216efc1093d424d335ad) if no user is currently logged in; otherwise, the page is blank
- https://ww.xx.yy.zz/start.html - [start](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/KpWxn_ktke79JixTh8UAgQ?section=Xbf3d5594d5fef020a4656378d3073627) page with general information about the CPU
- https://ww.xx.yy.zz/identification.html - [identifying information](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/yl7zlClN1FrkcWbdPEPU0w?section=Xb0b8b69aad8bca2cf848e4a08ef54022) about the CPU including serial, order, and version numbers, now called the Diagnostics page
- https://ww.xx.yy.zz/diagnostic.html - the [diagnostics buffer](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/9kXUDdUj5ShypnMNTjz3Gw?section=X842e9cd18ac6639aaf40d0b148b89d19)
- https://ww.xx.yy.zz/module.html - information about the [modules in the local rack and the ability to update firmware](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zkw1i6aTf022QhpONsl5wA?section=X9fd7e004bb711f264161b0cf27efe2e5)
- https://ww.xx.yy.zz/communication.html - [communication information](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3CtjZV~994YcPWji5oRs_Q?section=Xed857ed09e014090768e1f60ac08d2af) about the network addresses, physical properties of the communication interfaces, and communication statistics
- https://ww.xx.yy.zz/variable.html - [CPU variables (tags) and I/O](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f7WatsxclQNha2u2VG9y0g?section=X37eac0b13e3c4cc90b9bdcbd15642672), accessible by address, PLC tag name, or data block tag name
- https://ww.xx.yy.zz/watch.html - [watch tables](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/slqDdcEVd6jLXnTqF9vRPg?section=Xc90b523b21099b5ef9875b12ea0cf151)
- https://ww.xx.yy.zz/datalogs.html - download, delete, or retrieve and clear [Data Logs](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/mZZAYWI3qGGsoDurXWiHRQ?section=X99e5f10f7bebfbb0e13313f2836182a3)
- https://ww.xx.yy.zz/userfiles.html - [User Files](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/1oN_XWyhd4NVq8KmgLmtGA?section=X1a6c6a1b16f3caba9eb4fe292b939ccf) provides access to files on the SIMATIC memory card (external load memory)
- https://ww.xx.yy.zz/filebrowser.html - [browser for accessing data log files or recipe files](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f1bXzgmsxyQgQcYAqC77rA?section=X81170b06653aefc28fb2399202cdb341) stored internally in the CPU or on a memory card
- https://ww.xx.yy.zz/index.html - [introduction page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829) to enter the standard Web pages

For example, if you enter "https://ww.xx.yy.zz/communication.html", the browser displays the communication page.

Note:

Note that any standard Web page that is not listed specifically above (for example, the [Online backup page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/isBliVNTXNJ6NCzfBBr7pg?section=X10d08635decfd77ea365a39fc4668fd0)) does not have a direct access URL.

## Secure access

Use a secure Virtual Private Network (VPN) to connect to the S7-1200 PLC Web server from a location outside your protected network. Require and use https:// instead of http:// for [secure access](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zhgg0gJgOhxaX6BVSPQiIA?section=Xd1f721b46269feb9a0bd64cba8b230f3) to the standard Web pages. When you connect to the S7-1200 with https://, the Web site encrypts the session with a digital certificate. The Web server transmits the data securely and it is not accessible for anyone to view. You typically get a security warning that you can confirm with "Yes" to proceed to the standard Web pages. To avoid the security warning with each secure access, you can [import the Siemens software certificate to your Web browser](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/MLhOdcBjbS9SxLjBtqsreA?section=X44c4d41f5bfe40d423bb36671a63bfa0).

---

## Accessing the Web pages from a mobile device

To access an S7-1200 from a mobile device, you must connect your PLC to a network that connects to the Internet or to a local wireless access point. Use a secure Virtual Private Network (VPN) to connect a mobile device to the S7‑1200 PLC Web server. You can use port forwarding in the wireless router to map the IP address of the PLC to an address by which a mobile device can access it from the Internet. To configure port forwarding, follow the instructions for the software configuration of your router. You can connect as many PLCs and switching devices as your router supports.

Without port forwarding, you can connect to a PLC, but only locally within range of the wireless signal.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/XrjEdxFtTleZmOi8idJ9uA-VBkTPlmjVZAl17lebjV9hA/content?v=30350d0ddaa3327a)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/XrjEdxFtTleZmOi8idJ9uA-VBkTPlmjVZAl17lebjV9hA)

In this example, a mobile device that is within range of the local wireless access point can connect to PLC 3 and PLC 4 by their IP addresses. From the Internet outside the local wireless range, a mobile device can connect to PLC 1 and PLC 2 using the port forwarded address for each PLC.

To access the standard Web pages, you must have access to a cellular service or wireless access point. To access a PLC from the Internet, enter the port forwarded address in the Web browser of your mobile device to access the PLC, for example http://ww.xx.yy.zz:pppp or https://ww.xx.yy.zz:pppp, where ww.xx.yy.zz is the address of the router and pppp is the port assignment for a specific PLC.

For local access through a local wireless access point, enter the IP address of the S7‑1200 CPU or a [Web server-enabled CP](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/H8v_ZyWzJV4IpD~luNGAwg?section=X05a9645e263fbf69039c35b0ff635f64) in the local rack:

- http://ww.xx.yy.zz or https://ww.xx.yy.zz to access the [standard Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/wYbAoKDX_XQ_9F0P~5rJkg?section=X165292e35124f741a26d2259be560c6f)
- http://ww.xx.yy.zz/basic or https://ww.xx.yy.zz/basic to access the [basic Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/mlhbK0vfPzNGjGOQTfxulw?section=X9cfbdd5e92998f97ce9002f6b86a1419)

For increased security, configure the Web server to be accessible only by [secure access (HTTPS)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zhgg0gJgOhxaX6BVSPQiIA?section=Xd1f721b46269feb9a0bd64cba8b230f3).

---

## Using a CP module to access Web pages

Regardless of whether you access the Web server from a PC or a mobile device, you can connect to standard Web pages through one of the following CP modules when you have configured it in STEP 7 and installed it in the local rack with the S7‑1200 CPU:

- CP 1243-1
- CP 1243‑7 LTE‑EU
- CP 1243‑7 LTE‑US
- CP 1243-8 IRC

You use the [Start standard Web page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/KpWxn_ktke79JixTh8UAgQ?section=Xbf3d5594d5fef020a4656378d3073627) to access the Web pages through these CP modules. The Start page displays all configured and installed CP modules that you have in your local rack, but you can only access Web pages from the ones listed above.

Note:

**Access to standard Web pages when Web server-enabled CPs are in the local rack**

You might observe delays up to one or two minutes when connecting to the S7-1200 standard Web pages when Web server-enabled CPs are in the local rack. If the pages do not appear to be available, or you get errors, just wait one or two minutes and refresh the page.

---

## Web server security certificates

You can create certificates for the CPU in the device configuration of an S7-1200 CPU. This feature is available under the "Protection & Security > Certificate manager" general setting for the device.

You can create certificates for the Web server from "Web server > Security" in the device configuration for the CPU. Web server certificates are software downloaded, which enables you to use your own custom certificate.

Refer to the STEP 7 Information System for more information about certificates and also the topic [Supported certificates](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/0HuKkB3PdN5AHLWA2Zf0Zw?section=Xadd2fa9c957dbb69c387358bec35ae05) in this document.

Note:

**S7-1200 certificate limit**

The S7-1200 has a system certificate limit of 64.

All certificates count against this number (for example, Web server certificates, OPC UA certificates, and OUC certificates).

If the Web server certificate has been signed by a Certificate authority (CA) certificate and present in the TIA Portal, then 2 certificates are used by the Web server (one for the Web server certificate and one for its downloaded CA certificate).

If you have more than 64 certificates, the TIA Portal displays an error that states that you have exceeded the maximum number of 64 certificates. You must remove some certificates from the PLC configuration.

## Working with certificates that are not self-signed

If you are not using self-signed certificates, use the "download certificate" link from the [Introduction page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829) to download the Siemens security certificate to your PC. The procedure for downloading and importing varies according to which Web browser you use. The "download certificate" link is not active when using self-signed certificates.

To import and install the Siemens certificate, follow the conventions of your Web browser.

After you install the Siemens security certificate "S7-1200 Controller Family" in the Internet options for your Web browser content, you do not have to verify a security prompt when you access the Web server with https:// ww.xx.yy.zz.

---

## Standard Web pages


---

### Layout of the standard Web pages

Each of the S7‑1200 standard Web pages has a common layout with navigational links and page controls. Regardless of whether you are viewing the page on a PC or on a mobile device, each page has the same content area, but the layout and navigation controls vary based on the screen size and resolution of the device. On a standard PC or large mobile device the layout of a standard Web page appears as follows:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/~tVHoqVpte77wwH~5D_46A-VBkTPlmjVZAl17lebjV9hA/content?v=90598be8c87591a6)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/~tVHoqVpte77wwH~5D_46A-VBkTPlmjVZAl17lebjV9hA)

|  |  |
| --- | --- |
| ① | Web server header with selector to display PLC Local time or UTC time, and a selector for the [display language](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/_C8a5oVebCK6~uYTvFACfg?section=X89e4777dcbcade2d6f2908668dc09468) |
| ② | Log in or log out |
| ③ | Standard Web page header with name of the page that you are viewing. This example is the CPU Diagnostics > Identification page. Some of the standard Web pages, such as module information, also display a navigation path here if multiple screens of that type can be accessed. |
| ④ | Refresh icon: for pages with automatic refresh, enables or disables the automatic refresh function; for pages without automatic refresh, causes the page to update with current data |
| ⑤ | Print icon: prepares and displays a printable version of the information available from the displayed page |
| ⑥ | Navigation area to switch to another page |
| ⑦ | Content area for specific standard Web page that you are viewing. This example is the Diagnostics page. |

Note:

**CP module standard Web pages**

[Certain CP modules](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/H8v_ZyWzJV4IpD~luNGAwg?section=X05a9645e263fbf69039c35b0ff635f64) provide standard Web pages that are similar in appearance and functionality to the S7‑1200 CPU standard Web pages. Refer to your CP documentation for descriptions of the CP standard Web pages.

---

### Basic pages

The Web server provides basic pages intended for use on mobile devices. You access the basic pages using the IP address of the device and appending "basic" to the URL: http://ww.xx.yy.zz/basic or https://ww.xx.yy.zz/basic

The basic pages look similar to the standard pages, but with some differences. The page omits the navigation area, login area, and the header area, and includes buttons for advancing backward and forward through the Web pages. Basic pages also include a Home page button that takes you to a Navigation page. You can also use the navigation controls provided with your mobile device for navigation. For example, the basic Diagnostics page appears as follows in the vertical orientation:

The minimum resolution for displaying a basic page is 240 x 240 pixels.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/kCxh_hfSV3YENul7qsOMqA-VBkTPlmjVZAl17lebjV9hA/content?v=d6373def24164e00)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/kCxh_hfSV3YENul7qsOMqA-VBkTPlmjVZAl17lebjV9hA)

Note that the standard Web page illustrations in this chapter represent the standard PC Web page appearance. Most of the standard Web pages have equivalent basic pages.

---

### Logging in and user privileges

Each of the PC standard Web pages provides a login window above the navigation pane. Due to space considerations, the basic Web pages provide a separate Login page. You assign the following user privileges under Security settings > Users and roles in the project tree:

- Change operating mode
- Change web server default page
- Read diagnostics
- Read syslog buffer on the CPU
- Flash LEDs
- Perform a firmware update
- Change time settings
- Create a backup of the CPU
- Restore the CPU using a backup file
- Download service data
- Change parameters of the F-System (F-Admin)1
- Read process data
- Read process data of the watch tables
- Write process data
- Write process data of the watch tables
- Open user-defined web pages
- Write process data through commands of the automation web page programming (AWP)
- Read files
- Write/delete files

1 Available for Failsafe CPUs only.

## Logging in

To perform certain actions such as changing the operating mode of the controller, writing values to memory, and updating the CPU firmware you must have the required privileges.

Note that if you have set the [protection level of the CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/boJrawCTV7~GzOYPMsNOtA?section=X6b7b6de0ce1887813501b51c2fcc624a) to "Complete protection (no access)", then the "Anonymous" user does not have permission to access the Web server, regardless of the Web server user permission settings.

Warning:

**Unauthorized access to a CPU**

Users with CPU full access or full access (incl. fail-safe) privileges have privileges to read and write PLC variables. Regardless of the access level for the CPU, Web server or OPC UA users can have privileges to modify PLC data and execute functions. Unauthorized access to the CPU can disrupt process operation.

Siemens recommends that you observe the following security practices:

- Enable [Access control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7nIuqWCd4bYr85ym87r3Cg?section=Xacdebbc7e299aa37867bfd6f048080e1) under "Protection & Security > Access control".
- Do not enable the "Anonymous" user.
- Use strong passwords, as defined in STEP 7.
- Enable the setting "Only allow secure PG/PC and HMI communication" under "Protection & Security > Connection mechanisms".
- Use a secure Virtual Private Network (VPN) to connect to the S7-1200 PLC from a location outside your protected network.
- Enable access to the Web server only with the HTTPS protocol.
- Perform error-checking and range-checking on your variables in your program logic because Web server or OPC UA users can change PLC variables to invalid values.
- For the OPC UA server: In your STEP 7 Device configuration, navigate to "Properties > OPC UA > Server > Security" and deselect "No security" in "Security policies available on the server for the secure channel".

Disruption of process operations can result in death, severe personal injury, and/or property damage.

The log in frame is near the upper left corner on each standard Web page when displayed from a PC or a wide mobile device.

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAAAnCAIAAABIRdfKAAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH3AgeFBcpdYAKzwAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAAEIElEQVRoge2ZXWsjVRjH/2fekmY63by3nU2T1G23NDFN1gQrIiLileCNioj3gp9AivTSiwW/xbLi4oJeuCy4LEXwYqmuK1q6UrVN0ua17TadNGlemsl4Eah1tk0bts3EzfldDGdmTp7nOfznec7JOeTbOwugGAdjdAD9DhXAYKgABkMFMBgqgMFwunuPPDw14TMklF5g5e9kKpPvpke9AILAS5LYzQh6CkHgu+yxXQmq1w+ObVPOkXYCPPrtj2PblHNEX4JOpdFoAGBZlhCiaZqqqgA4jgOgqipACCEaNE3TCAjLMgBUtalpTYZhGIZpNpsAaTZVhmFASFNVjzXVP3Q22q3twnoqC0AecY2OuNLZzfzmEwA+r+y0W3988MjttLucttV4amDAzLHsuP8ygHgiXa3VLJaBK37PRjpXqdZqtbokiQxhlOLesNvhkYdz+e1MbguA1zPqctouYKQ9SmfL0NX4RjQSiEYCJkEAkErno5FA+MWpeDINgIB4x0ZNgkAIM311XBQHlGKJEOL3ydFIQGtq1WoNAM9x0UhAKZaGJDEaCaTSeQDJjWzL8mp84wKG2bt0lgGzsdDiwyUAfq8MoFqrt27t9ksATCZhULQUiyVp0HK4nCBAPJkulyvFUtkjuwHYbZdarw4bAA4OGi1TNuvQs4/qf0S7DHA57ZtbTwBk81vDbgeA1XhqNhaajYVan7zZJMzGQrFrQZZlTzJSUPYGRUtw+grLtPPF81zLchtTzyXtMmDcdzmxno4nl4bdDp9XBuD3yq3vNByaAhAKTi4+XGIYci08DWBIEgGwLGuxmAGYTQLP8zartJZIx5MZv1dmWdZsNvE8B0AaFAnB4a/CoamW5WgkcLEj7jGI7jzgBb9nJjhpVDSG8/vyX2uJVDc90r0gg9GXoJ2C8nhlzZBQeoGdgtJlj3oBdpW9XWWvy0H0M7QEGQwVwGD0JWhIEo/+P+o3dgpKca/cTY96AZwOW58vQ7ssAC1BBkMFMBgqQGfkshVFqZ+x858rxVP7UAE64+efdpKJs04SlYp6ap/+On46d7KZ/a9vrVf21dffcL/6miuZKH11MxkKW5eXdj/9LHj/XjYcsX1x/fFM2PrrL4X3PhibvKrfbKcZ8EzcvZP58CPf3Hzwh4U8gC9vJObmg54xS7ncAFCrNgFU9lWXyzw3H7x9a/1pC1SA8yccsZlM/55qcBx5KWY/qTMV4PxZfLBdrZ5e/VvQOaAzRJH95vbG3e8yAHx+8d33x27eSJRLjbffkQF8/MnE9c+XX37FwfMMAJtdOLwebRyFHsj8h/YHMuXSwb3vc2exs3A/9+ZbI08/D81YJyalo0/0GdBQ1WrtrOvc54+G2q508AIzHTjTRtlJ3ewOfRLoM4DSZegkbDBUAIOhAhjMP/TLYHIU1VmoAAAAAElFTkSuQmCC)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/wYK4UYuaRJen6HwTI4S_~w-VBkTPlmjVZAl17lebjV9hA)

The Log In page is a separate page on small mobile devices that display the basic pages. It is selectable from the Home page.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/MEUex1_LOFQ8MivWeZCvQw-VBkTPlmjVZAl17lebjV9hA)

The Log In screen might also display in the main frame, for example, during a Restore operation.

Your login session expires after thirty minutes of inactivity. If the currently-loaded page is continually refreshing, the login session timeout resets, preventing the session from expiring.

Note:

If you encounter any problems logging in, [download the Siemens security certificate](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/MLhOdcBjbS9SxLjBtqsreA?section=X44c4d41f5bfe40d423bb36671a63bfa0) from the [Introduction page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829). You can then log in with no errors.

## Logging out

To log out, simply click the "Logout" link from any page when viewing from a PC or wide mobile device.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/NLqo~h0_5DR4YKKriwVrWA-VBkTPlmjVZAl17lebjV9hA)

From the basic pages, navigate to the Login/Logout page from the Home page and tap the "Logout" button.

[![](data:image/png;base64,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CAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjABMICJhAWMIGwgAmEBUwgLGACYQETCAuYQFjAhEz8KzMz896uBzxk8IoFTPw/atmMw4I/7q0AAAAASUVORK5CYII=)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/fsbJfK03bU2_JLy53t39tg-VBkTPlmjVZAl17lebjV9hA)

After you log out, you can only access and view standard Web pages according to the privileges of the "Anonymous" user. Each of the standard Web page descriptions defines the required privileges for that page.

Note:

**Log off prior to closing Web server**

If you have logged in to the Web server, be sure to log off prior to closing your Web browser. The Web server supports a maximum of seven concurrent logins.

---

### Introduction

The Introduction page is the welcome screen for entry into the S7-1200 standard Web pages.

Figure 1. [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/w70l5qvaKjuwEPuB5Gqrsw-VBkTPlmjVZAl17lebjV9hA/content?v=8591b89195667a66)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/w70l5qvaKjuwEPuB5Gqrsw-VBkTPlmjVZAl17lebjV9hA)

From this page, you click "Enter" to access the S7-1200 standard Web pages. At the top of the screen are links to useful Siemens Web sites, as well as a link to [download the Siemens security certificate](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/MLhOdcBjbS9SxLjBtqsreA?section=X44c4d41f5bfe40d423bb36671a63bfa0). You can also choose to skip the introduction page on future accesses to the Web server.

---

### Start

The Start page displays a representation of the CPU or CP to which you are connected and lists general information about the device and the TIA Portal version you used to download the project to the CPU. For the CPU, you can use the buttons to change the operating mode and flash the LEDs, if you have [logged in](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nDYnYbhrwbHcYZyUn7lygQ?section=Xf14b550dd189216efc1093d424d335ad) with the "Change operating mode" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785).

The bottom portion of the screen is visible if you have configured and installed [Web server-enabled CP modules](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/H8v_ZyWzJV4IpD~luNGAwg?section=X05a9645e263fbf69039c35b0ff635f64) in the local rack with the S7‑1200 CPU. You can hover over and click a Web server-enabled CP module to access the standard Web pages. Refer to the documentation for your CP module for information about the CP module Web pages. You see the name of the CP module when you hover over it.

The Web server also displays any other CM and CP modules in the local rack, but you cannot click them as they do not contain Web pages. The module appearance for these CMs and CPs are light gray (desensitized) to indicate that they are display-only and not clickable modules.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/R7wmKjPzyh_RXsxoBEUSXA-VBkTPlmjVZAl17lebjV9hA/resized-content?v=eff03239a5413425)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/R7wmKjPzyh_RXsxoBEUSXA-VBkTPlmjVZAl17lebjV9hA)

Note that the S7-1200 fail-safe CPUs display additional data on this page related to functional safety.

---

### Diagnostics

The Diagnostics page displays the following information:

- Identification: identifying characteristics of the module and plant and location information from STEP 7
- Program protection: status of know-how protection and CPU binding, which can be useful in planning for spare parts as well as STEP 7 configuration setting for allowing or preventing the copy of internal load memory to external load memory (SIMATIC memory card).
- Memory: load, work, and retentive memory usage

F-CPUs display an additional Fail-safe tab.

Viewing the Identification page requires the "Read out diagnostics" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785).

## Identification tab

The Identification tab includes the following information:

- Order Identification: Displays Plant designation, Location identifier, and Serial number
- Order Number: Displays the order number for the PLC
- Version: Displays version identification for both the PLC and the firmware

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/doYjftvZ92i4hz7DEDgmMA-VBkTPlmjVZAl17lebjV9hA/content?v=d40024f378183924)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/doYjftvZ92i4hz7DEDgmMA-VBkTPlmjVZAl17lebjV9hA)

## Program protection tab

The program protection tab includes the following information:

- [Know-how protection](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/QHw~mfwuSzKV9AZLKNqsYw?section=Xc2e06ca3350b2e8e8e3c069896da8203): Displays whether you have configured know-how protection for any of the program blocks in STEP 7
- [Binding](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/uPySt3Pz5TRLltQsxMhX9g?section=Xa63b7a68c88ce8e0e33341135882c9bc): Displays whether you have bound the program to either the CPU or to the SIMATIC memory card
- [Program copy to memory card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/tyZyJoRQfEvwKPv4arAn1w?section=Xd4cdbb395e6f69a1f827cc106a54d06d): Displays whether you have enabled the ability to copy the program from internal load memory to external load memory (SIMATIC memory card)

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/vWHe08~OpMLbqleHV~ebxw-VBkTPlmjVZAl17lebjV9hA/content?v=73288f51f14b636c)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/vWHe08~OpMLbqleHV~ebxw-VBkTPlmjVZAl17lebjV9hA)

## Memory tab

The [Memory](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/_qn0HH3iWGT1U1b5T0vF7A?section=X1e81f6906f2a226872ed34290b5cd417) tab includes the following information:

- Load memory: Displays usage as a percentage and Free/Total available in MB
- Work memory: Displays usage as a percentage and Free/Total available in KB
- Retentive memory: Displays usage as a percentage and Free/Total available in KB

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/G9dWJn3HeL4nseWcXo55fQ-VBkTPlmjVZAl17lebjV9hA/content?v=ff667f546b3a3970)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/G9dWJn3HeL4nseWcXo55fQ-VBkTPlmjVZAl17lebjV9hA)

## Fail-safe tab

Refer to the [S7-1200 Functional Safety Manual](https://support.industry.siemens.com/cs/ww/en/view/104547552) for information about the Diagnostics page Fail-safe tab.

---

### Diagnostics Buffer

The diagnostics buffer page displays diagnostic events. The newest event is Number 1 at the top. The oldest event is Number 50. From the selector on the left, you can choose what range of diagnostics buffer entries to display, either 1 to 25 or 26 to 50. From the selector on the right, you can choose whether to display the times in UTC times or PLC local times. The top part of the page displays the diagnostic entries with the time and date of when the event occurred.

You can select any individual diagnostic entry to show detailed information about that entry in the bottom part of the page. Note that the display language of the diagnostics buffer entries depends upon your device configuration setting for [multilingual support](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/pXRGRupChjj9fJ2M77PwfQ?section=X6e0442c492f12bebac44dc65d0dfc30a).

You must configure the languages used for diagnostic text in the TIA Portal project downloaded to the PLC. This configuration is available in the PLC properties under "Multilingual support". Each language downloaded must be associated with a supported webserver language. The PLC is limited to 2 downloaded languages.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/8TVRJXPUhWPpuj96LBprKA-VBkTPlmjVZAl17lebjV9hA/content?v=ac1b11e65d818b03)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/8TVRJXPUhWPpuj96LBprKA-VBkTPlmjVZAl17lebjV9hA)

The Diagnostics Buffer page also includes a [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAWCAIAAACg4UBvAAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH4goZEiQ20QkTvAAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAACAUlEQVQ4jc2TS2gTURSG/3PvzWRCByc1xMYHuIgvqAWloCDuLEoh4EKpVagudCFdim5duHIjoiiI0pXdGKXgA9pCQNyG4AMf1IJGawvRampTjMncmXtcNhlNNl3Uf3fgfPc/5/IfKhQKWIHESuD/gFeNRamCzHWDCHUlHSsmYUvYkm0FW2pJ32cqXP726ISVcsS/eQBYnIPwH1w62L0x6gWB53MtMHVtXs/7Q8+LWCiD0y39AdD6NEu6eiXbFa0ODh0aufNk4FT/vbuTfcczJDVt3QHo1vsTwZIkaWzs2ZFjB77Mztc8vTbZeX900l9a5JkpGAajDQ/YElIA2LA5tXvvTje+Jp+fmng5eubsDdF/Etqg+YGwP9kSSuzq3T58+vLbN8VXL6Ydt0Mb3tazhQPD2oT8qTF/pao4PN4JwuAeJxFXgSAfCAxrwz+W/IlP4HcfHw5QypUt/o+AmKIOlZ0DlUERgiQwWBuuKWLfeAaQjUSIJ4opiqpcxulJLPdtOvehWjPkROAZcDsesCSUsBUl+m7v6143cmE/AJl2xUKdv1bhGzRLNONEEUGSQk3mt0ZVI+C/+SZ/NxIcFcXs09LF9wrA9Gzl/K08gHoxYI/hG/j18ce9N6+lAMTjQS73mUL3X/PMz19NCQsp6VpSLA8Yzq9tiZQVbcOHtNr3v9r8H8bVx1n4f2v5AAAAAElFTkSuQmCC)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/PrnkrOw8AkNjmm2ogWMYvA-VBkTPlmjVZAl17lebjV9hA) button to save the diagnostics buffer to a CSV file. By default, the Web server saves the comma-separated file to ASLog.csv in your Downloads folder. The file contains the complete diagnostics buffer at the time of the save operation. You can save the file as many times as you choose and keep multiple files. You can open the diagnostics buffer file with Microsoft Excel or any text editor.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/RSi35AONYm7LXb_8naMrkQ-VBkTPlmjVZAl17lebjV9hA/content?v=10081081fd797162)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/RSi35AONYm7LXb_8naMrkQ-VBkTPlmjVZAl17lebjV9hA)

Viewing the Diagnostics Buffer page requires the "Read out diagnostics" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785).

---

### Module Information

The module information page provides the following:

- Information about all the modules in the local rack
- The capability to perform a firmware update
- Information about distributed I/O systems

The top section of the screen shows a summary of the modules based on the device configuration in STEP 7, and the bottom section shows status, identification and firmware information for the selected module based on the corresponding connected module.

Viewing the Module Information page requires the "Read process data" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785).

## Module information: State tab

The state tab in the bottom section of the module information page displays a description of the current state of the module that is selected in the top section. If the section is empty, then the module has no pending diagnostic state.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/vcpEWYZP_gZrz6DK6WCxkw-VBkTPlmjVZAl17lebjV9hA/content?v=f2d8ba42e61a51f7)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/vcpEWYZP_gZrz6DK6WCxkw-VBkTPlmjVZAl17lebjV9hA)

## Status icons for the modules

For each module, the status column of the top section displays an icon that indicates the status of that module:

| **Icon** | **Meaning** |
| --- | --- |
|  | No fault |
|  | Deactivated |
|  | Maintenance required |
|  | Maintenance demanded |
|  | Error |
|  | The CPU cannot reach the module or device (for devices other than the CPU) |
|  | The CPU has established a connection to the device, but the module status is unknown (for devices other than the CPU) |
|  | Input and output data are unavailable because the submodule has blocked its I/O channels (for devices other than the CPU) |

## Navigating

You can select a link in the top section to navigate to the module information for that particular module. Modules with submodules have links for each submodule. The type of information that is displayed varies with the module selected. For example, the module information dialog initially displays the name of the S7‑1200 station, a status indicator, and a comment. If you click the CPU name, the module information displays the following:

- Name of the digital and analog inputs and outputs that the CPU model provides,
- Addressing information for the I/O
- Status indicators
- Slot numbers
- Comments

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/fBAk4qSb1SSAIxR_kAcWnQ-VBkTPlmjVZAl17lebjV9hA/content?v=b16504f148e4637e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/fBAk4qSb1SSAIxR_kAcWnQ-VBkTPlmjVZAl17lebjV9hA)

The module information page shows the path you have followed. You can click any link in this path to return to a higher level.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/HCO0nZzeaV9DxQjImrfEDA-VBkTPlmjVZAl17lebjV9hA)

## Module information: Identification tab

The identification tab displays the Identification and Maintenance (I&M) information of the selected module.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/E1E_VzvgGj2c_Wx53KVYpA-VBkTPlmjVZAl17lebjV9hA/content?v=7e9828f3b5bbb98c)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/E1E_VzvgGj2c_Wx53KVYpA-VBkTPlmjVZAl17lebjV9hA)

Note that if you click an F‑I/O module in the top section, then the bottom section has a Safety tab. On this tab, you can see specific data related to the selected module as described in the [S7-1200 Functional Safety Manual](https://support.industry.siemens.com/cs/ww/en/view/104547552).

---

### Updating firmware

## Module information: Firmware tab

The firmware tab of the module information page displays information about the firmware of the selected module. If you have the "Update firmware" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785), you can also perform a firmware update of the CPU or other modules in the local rack that support firmware update or PROFINET I/O modules. For remote modules, you can view the firmware information, but not perform a firmware update.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/RWQ8T0ybu3WA_qp4R3LSvg-VBkTPlmjVZAl17lebjV9hA/content?v=148a33a60ab0b4e6)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/RWQ8T0ybu3WA_qp4R3LSvg-VBkTPlmjVZAl17lebjV9hA)

## Performing a firmware update

The CPU must be in STOP mode to perform a firmware update. When the CPU is in STOP mode, click the Browse button to navigate to and select a firmware file. Firmware updates are available on the [Siemens Industry Online Support Web site](http://support.industry.siemens.com).

During the update, the page displays a message showing that the update is in progress. After the update completes, the page displays the article number and version number of the updated firmware. If you updated the firmware for the CPU or a signal board, the Web server restarts the CPU.

You can also perform a firmware update by one of these methods:

- Using the [online and diagnostic tools of STEP 7](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/9gNUHfi5FIIkXHkF6~odTQ?section=X676c3f3fbf8cda818420f7b5a9b8a3db)
- Using a [SIMATIC memory card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/2_4~8k2RDOs~~ji0BO4dRQ?section=Xe2bb67aff193f4fb2925b9ca97391dce)
- Using the [SIMATIC Automation Tool](https://support.industry.siemens.com/cs/ww/en/view/98161300)

Note:

The firmware update process discards any additional data appended to the firmware update file. Appending data to a firmware update file has no effect on the firmware update or the S7-1200 CPU. You cannot append data, for example, to add components.

Note:

**Potential problems with performing a firmware update from the Web server**

In the event of a communications disruption during a firmware update from the Web server, your Web browser could display a message asking whether you want to leave or stay on the current page. To avoid potential problems, select the option to stay on the current page.

If you close the Web browser while in the process of performing a firmware update from the Web server, you will be unable to change the operating mode of the CPU to RUN mode. If this situation happens, you must cycle power to the CPU to be able to change the CPU to RUN mode.

---

### Communication

The communication page displays the following:

- Parameters of the connected CPU
- Communications statistics
- Connection resources
- Information about connections

Viewing the Communication page requires the "Read process data" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785).

## Parameter tab

The Parameter tab shows the following information:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/ulQLYWskZvQyzckVgkiGPQ-VBkTPlmjVZAl17lebjV9hA/content?v=5660c762e53299c7)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ulQLYWskZvQyzckVgkiGPQ-VBkTPlmjVZAl17lebjV9hA)

## Statistics tab

The Statistics tab shows send and receive communication statistics:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/9rUiwyon7X8E9ck7Pv_oFg-VBkTPlmjVZAl17lebjV9hA/content?v=4bc08e6d994741f5)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/9rUiwyon7X8E9ck7Pv_oFg-VBkTPlmjVZAl17lebjV9hA)

## Connection resources tab

The Connection resources tab shows information about the total number of connection resources and how they are allocated for different types of communication:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/00lyt09Gyd11n2JJfKWB0w-VBkTPlmjVZAl17lebjV9hA/content?v=44ec11fd0211f4ee)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/00lyt09Gyd11n2JJfKWB0w-VBkTPlmjVZAl17lebjV9hA)

## Connection status tab

The Connections status tab shows the connections for the CPU, and connection details for the selected connection.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/1UieSo~LatFoWUxl0jQDxg-VBkTPlmjVZAl17lebjV9hA/content?v=0e2aba7f1a7576bd)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/1UieSo~LatFoWUxl0jQDxg-VBkTPlmjVZAl17lebjV9hA)

---

### Tag status

The Tag status page allows you to view any of the I/O or memory data in your CPU. You can enter a direct address (such as %I0.0), a PLC tag name, or a tag from a specific data block. For data block tags, you enclose the data block name in double quotation marks. For each monitor value you can select a display format for the data. You can continue entering and specifying values until you have as many as you want within the limitations for the page. The monitor values show up automatically. You can click the "Refresh" button at any time to refresh all of the monitor values. If you have [enabled automatic update in STEP 7](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zhgg0gJgOhxaX6BVSPQiIA?section=Xd1f721b46269feb9a0bd64cba8b230f3), you can click the "Off" icon in the upper right area of the page to disable it. When automatic update is disabled, you can click "On" to re-enable it.

You can view the Tag status page if you have the "Read process data" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785).

If you [log in](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nDYnYbhrwbHcYZyUn7lygQ?section=Xf14b550dd189216efc1093d424d335ad) as a user with the "Write process data" privilege, you can also modify data values. Enter any values that you wish to set in the appropriate "Modify Value" field. Click the "Go" button beside a value to write that value to the CPU. You can also enter multiple values and click "Apply" to write all of the values to the CPU. The buttons and column labels for modifying only appear if you have the necessary privilege.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/ZOFj2HE9juEVDS_B41_ATQ-VBkTPlmjVZAl17lebjV9hA/content?v=d95fde3126aabc8e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ZOFj2HE9juEVDS_B41_ATQ-VBkTPlmjVZAl17lebjV9hA)

If you leave the Tag status page and return, the Tag status page does not retain your entries. You can bookmark the page and return to the bookmark to see the same entries. If you do not bookmark the page, you must re-enter the variables.

For values you frequently monitor or modify, consider using a [Watch table](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/slqDdcEVd6jLXnTqF9vRPg?section=Xc90b523b21099b5ef9875b12ea0cf151) instead.

Note:

Be aware of the following information when using the standard Tag status page:

- Enclose all string modifications in single quotes.
- The Tag status page can monitor and modify tags that contain any of the following characters: &, <, (, +, ,(comma), ., [, ], $, or %, providing you enclose the tag name in double quotation marks, for example, "Clock\_2.5Hz".
- To monitor or modify just one field of a DTL tag, include the field in the Address, for example, "Data\_block\_1".DTL\_tag.Year. Enter an integer value for the modify value according to the data type of the specific field of the DTL. For example, the Year field is a UInt.
- The maximum number of variable entries per page is 50.
- If a tag name displays special characters such that it is rejected as an entry on the Tag status page, you can enclose the tag name in double quotation marks. In most cases, the page will then recognize the tag name.

**See also**

[Rules for entering tag names and values](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3vX3qw38C~jcPesOy~gETg?section=X3c7ba9e2c6060316eda5aa53f6a47736)

---

### Watch tables

The Web server allows you to access watch tables that you have configured in STEP 7 and downloaded to the CPU. Watch tables with 50 or fewer entries offer the best performance in the Web server. Exceeding 50 entries might degrade system performance or cause watch table access errors.

## STEP 7 configuration to select watch tables for the Web server

From the Device configuration of the CPU in STEP 7, you can add the watch tables that you want the Web server to be able to display. For each watch table that you select from the list of existing watch tables, you select Read or Read/Write privileges for it in STEP 7. When downloaded to the CPU, you can only view the watch tables that have the Read privilege but you can view and modify watch table tags when you select the Read/Write privilege.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/IhezBp3wrkBlECFuO0HacA-VBkTPlmjVZAl17lebjV9hA/content?v=7a39fabbfe7f2f2a)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/IhezBp3wrkBlECFuO0HacA-VBkTPlmjVZAl17lebjV9hA)

After you complete the watch table configuration in the Web server section of the device configuration, download your hardware configuration to the CPU.

## Viewing watch tables from the Web server

From the Web server, if you have the "Read process data of the watch tables" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785), you can select "Watch tables" from the navigation menu to access the watch tables that you have configured and downloaded to the CPU. If you have downloaded more than one watch table, you can select the one you want to display from the drop-down list. The Web server displays the watch table that you created in STEP 7 and the current values according to the display format. You can change the display format if you choose, but when you return to the watch table page the Web server defaults to the display formats in the STEP 7 watch table.

## Modifying watch table tags from the Web server

If you downloaded a watch table with the "Read/Write" access level, you must log in to the Web server as a user with "Write process data of the watch tables" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785) to modify tag values just like you do in a watch table in STEP 7. You can modify individual tag values and click "Go" to modify only the one value, or you can enter several values and click "Apply" to modify them all at once.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/1oyIuKxJHH_rxIor4GgTjQ-VBkTPlmjVZAl17lebjV9hA/content?v=5abe369fe621276a)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/1oyIuKxJHH_rxIor4GgTjQ-VBkTPlmjVZAl17lebjV9hA)

Note:

**Advantages of watch tables for modifying tags**

For a user to modify tags and data block tags in the CPU from a watch table, you must configure the watch table in the Web server properties in the STEP 7 device configuration, and you must configure it for Read/Write access. By so doing, you can restrict the tags to which a user with the "Write process data of the watch tables" privilege can modify to only those tags in the configured Web server watch tables.

The [Tag Status](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f7WatsxclQNha2u2VG9y0g?section=X37eac0b13e3c4cc90b9bdcbd15642672) page, on the other hand, allows any user with the "write tag status" privilege to write to any tag or data block tag in the CPU.

By careful configuration of the Web server [user management privileges](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785), you can help safeguard access to your PLC data.

**See also**

[Rules for entering tag names and values](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3vX3qw38C~jcPesOy~gETg?section=X3c7ba9e2c6060316eda5aa53f6a47736)

---

### Online backup

The Online backup standard Web page allows you to make a backup of the STEP 7 project for the online PLC as well as to restore a previously-made backup of the PLC. Before creating a backup or restoring a backup, place the PLC in STOP mode and cease all communication with the PLC such as HMI access and Web server access. If your CPU is not in STOP mode, the backup and restore functions prompt for confirmation to place the CPU in STOP mode before continuing.

If you have accessed the Online backup page through one of the Web-enabled CP modules, you can perform a backup but you cannot restore.

Note:

You can also perform [backup and restore operations from STEP 7](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/riDJwjsjSBEP7d4A3ALAQA?section=X3bb82fb0da39d466969fc9011b950c1a). Refer to these topics for a full description of what data you can back up and restore. The SIMATIC Automation Tool also provides backup and restore capability.

When you back files up from the Web server, your PC or device saves the backup files in the default folder for downloads. When you back files up from STEP 7, STEP 7 stores the files within the STEP 7 project. You cannot restore STEP 7 backup files from the Web server and you cannot restore Web server backup files from STEP 7. You can, however, save STEP 7 backup files directly to the download folder of your PC or device. If you do so, then you can restore these files from the Web server.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/tc2k1QVvIgsUyF2GsIdpfQ-VBkTPlmjVZAl17lebjV9hA/content?v=33c016fde82743cc)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/tc2k1QVvIgsUyF2GsIdpfQ-VBkTPlmjVZAl17lebjV9hA)

## Backup PLC

From the Backup PLC section of the page, click the "Create online backup" button to make a backup of the project that is currently stored in the PLC. This function requires the "Create a backup of the CPU" user [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785). If the CPU is in RUN mode and you have to change it to STOP mode, you also need the "Change operating mode" privilege. The PC or device will store the backup file at the default location for downloads. Depending on your browser and device settings, you might be prompted about saving the file.

## Restore PLC

From the Restore PLC section of the page, enter the Web server user password and click the "Browse" or "Choose File" button (depending on your browser) to select a previously saved backup file. Click the "Load online backup" button and confirm the prompt to load this file in the connected PLC. This page requires the "Restore the CPU using a backup file" user [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785). If the CPU is in RUN mode and you have to change it to STOP mode, you also need the "Change operating mode" privilege.

As the restore operation proceeds, you see a series of progress messages and you must reenter your user login and password. After each step of the process completes successfully, you see the following completion indicators and a link to reload the page:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/~J9okbynLckO~sRc52CEdw-VBkTPlmjVZAl17lebjV9hA/content?v=1f408010288b2b94)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/~J9okbynLckO~sRc52CEdw-VBkTPlmjVZAl17lebjV9hA)

Warning:

**Restoring backups with unknown content**

If you restore a backup with unknown content, you can cause malfunctions or program errors. In addition, if you restore a backup that does not have the Web server enabled in the device configuration of the CPU, you will not be able to access the CPU from the Web server.

Make sure that the backup consists of a configuration with known content.

Malfunctions or program errors can cause death, severe personal injury and/or property damage.

Note:

**Restoring a backup where the CPU IP address is different**

If you attempt to restore a backup where the CPU IP address in the backup is different from the IP address of the current CPU, the Web server cannot display the message that the restore is complete. After you see the "Reset CPU" message for greater than five minutes, enter the new IP address that corresponds to the address in the backup file. The CPU now has this address, and you can resume Web server access.

---

### Data Logs

The Data Logs page allows you to access data logs.

The type of operations you can perform depends on your user [privileges](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785). Any user with the "Read files" privilege can view the files. If you have the "Write/delete files" privilege, you can also:

- Download a data log from your PLC to your computer
- Delete a data log from your PLC
- Retrieve and clear a data log

Data logs are displayed in ascending, case-insensitive, alphabetical order. The data log list is paginated in increments of 50 data logs.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/52rS2aYeOCT68FavTM73Lg-VBkTPlmjVZAl17lebjV9hA/content?v=fb8738532a16fc78)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/52rS2aYeOCT68FavTM73Lg-VBkTPlmjVZAl17lebjV9hA)

Note:

**Data log management**

Keep no more than 1000 data logs in a file system. Exceeding this number can prevent the Web server from having enough CPU resources to display the data logs.

If you find that the Data Logs Web page is not able to display the data logs, then you must place the CPU in STOP mode in order to display and delete data logs.

Manage your data logs to ensure that you only keep the number that you need to maintain, and do not exceed 1000 data logs.

## Working with a data log in Excel

The data log file is in USA/UK comma-separated values format (CSV). To open it in Excel on non-USA/UK systems, you must [Importing CSV format data logs to non-USA/UK versions of Microsoft Excel](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Rmy0jw5fbaEVmeCHBvPaEA?section=X093a26c805b4a2718773bea50e78cf44).

## Active state

The "Active" column on the Data Logs page shows "Yes" when there is a data log control block on the CPU associated with that file, and "No" when one does not exist. The active state can not be manually altered by the user.

If the STEP 7 program has a data log open or is writing to a data log, the Web server is unable to delete, download, or retrieve and clear the data log file. In addition, while the Web server is performing a download of a data log either through a download or a Retrieve and Clear, you can perform no other data log operation until the download is completed or canceled. The Web server displays an "Application Busy" error message.

## Download a data log file

You can download a data log file by clicking the file name. The Web server displays an error message if the file no longer exists or when another download is in progress. The error message remains on the page until you initiate an operation to reload the Data Logs page. The following operations cause the Web server to reload the Data Logs page:

- Refreshing the Data Logs page or navigating away and returning to the Data Logs page
- Changing the current Data Logs pagination selection
- Successfully deleting a data log
- Successfully retrieving and clearing a data log

Note:

**Data logs error message**

The Web server 's auto-refresh functionality does not remove the error message from the page.

The following scenarios generate error messages on the Data Logs page:

| **Operation** | **Failure condition** | **Error message** |
| --- | --- | --- |
| Download  Retrieve/Clear | - File does not exist - Invalid file name - Invalid HTTP request method - SMC is write-protected (Retrieve/Clear only) | Error while downloading the file |
| Delete | - Invalid HTTP request method - Invalid file name - File does not exist | Error while deleting the file |
| Delete | - SMC is write-protected | Error while deleting the file: memory card is write-protected |
| Delete | - User program is holding the data log file open | Application busy |
| Download  Delete  Retrieve/Clear | - Do not have required permission - HTTP request method is not POST or GET - Invalid ACTION parameter in URL | File operation not permitted |
| Download  Delete  Retrieve/Clear | - Invalid or missing HTTP referrer field | File operation not permitted: no referrer |
| Download  Delete  Retrieve/Clear | - User program is holding the data log file open - Currently downloading a data log | Application busy |
| Download  Delete  Retrieve/Clear | - Unexpected internal PLC error | Internal error |

## Deleting a data log

A data log cannot be deleted if it is open in the STEP 7 program. You must first close the data log before you can delete it. You can delete a data log by clicking the [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAIAAABvSEP3AAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH5gMOFR82s7ulQAAABANJREFUOI2NlF1PG0cUhs/M7rA2ttcyaxsLxS4fpRg7CNIWDCjUTZumogHUFilQKVLu8g9Q/kt7l5QbAheRUBJRcEIgFVDRBtMkNqVJSPgQIAwqu8Zez0cvTGziJlHP1Ugz550z533OoJ2dHQAAAIQQAAAIIeD9gRDCGAkhOD8+ik/sAcYIIfyO3HwIAJBlyWazWa3Wwp1yPl8IkUrpmQxzuWwWC3lXSYqiMCa2tlKp1LrTWe71qhhjIYQMABhjSlkyuZFIbAQC3lDolM/nkmWZUgqvH4kxUhQFY+nZs63p6fju7n5bW73X68AYM3asggBgZWV9eHjKVm658PUnPX2dNdU+mQCjLC9BCBECLy29GBmJrfy10XOxLRwOSBLKtyb/IgwA29upePxvztn+wWEux3t6OxsaqmQZTDOnKAql4teHS6Njs/H46umm6ubmWq/XZZq5Yl/yq4oKtbJS29rafPJkNZulupHp7+8Kh/xOp317+5+ZmeXhnyefJl+1ttb39Xac8ntMkxY8koaGho4tBoQxPjpiup7Z2dlbX981TVqhqZyJqalHP/04/vjxi6bm2sHBzyORBtVh5ZwX/S3wksnkdD29vLw2PBy7d++Pw8N0VZU7EgkpSlk8vrq5uReJBAd/OBeNNjlVG+f8pIlyYWWzKZpm1zTVYiH+gGd29s9k4uXk5CJjTJalSHvjpYFo19mwU7UJwUs4KKpwztNpkxC5s7NR05wIoZdr2/v7+wCi7sPqaLSlvb3R41FNk/0XpaKKEHkuRH4UGBWcCQCMkAQCDP0obWQoLa2iVOU1OGhvT5+Y+P3u3YX0UdYf8DnsNl0/Gh+f0zTV4bC63SoAFNw5Tiz2GaGyMnJ4mJmYWLx16+Hz568cqrX/+65r1y719bUfHBijow9isbhhmBiXzlqxFkVRMpnc3Fzi5s0H8fgqIZYzZ+q/udj2WVc4FArkcuzOnd/Gxma8XldHR9BiIYyxN1QQAgBkGNmFheT16xOLiytCiMZQoKc34vd7stlcXZ3v6tVuScKx2KMbN36RZNzW+pFFIYyzogrGmHORSKzdvj0/P//UMNL+gO/cF81dZ09rFappUknCtTW+K1fOSxKKxZZGRqatVqWlpVbCqHQCVLXc7XbY7dYyhfT2tn/3bWfA75EkxJiglGOMg0H/5ctfMsbn5hP37y+5PeoHfg1jxLmQ8w1HCNXUVHZ3f0oZp4xd+OrjpnA1wohSXqCJUggG/QMDUbvd6qqw0xwVIv9DiuIEYIwZY4aRFSDKrWWEECF4CRyShCllup4BQBYLIUQ69regkueFEBkAKGWMcXhbYIwJkTgXjLECNW9Qx7nIZnNvTT5xhmezpRe8/6/+v/EvPXIA4yoalWwAAAAASUVORK5CYII=)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/wuu7jJ3Aqn1deg1O8J7ffA-VBkTPlmjVZAl17lebjV9hA) icon in the Delete column for a specific data log. To delete the data log file, confirm the delete operation from the Delete dialog.

## Retrieve and Clear a data log

To open a data log and remove all entries, click the Retrieve and Clear [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAIAAABvSEP3AAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH5gMOFR8j3mZBqwAABCNJREFUOI1llMuOW0UQhv/qy7n4+Nhjj+eazAwJYkhCQIgFhA1C4gV4Al6HZ+AdWLFBIDbZwAIJBFGIhJAiwmgy8fhyxj4+l74Vi7GTIGrRXVKrSn//X3XTRVNmX33X/fJre7Tz7PNPik/fEoMAwWD8P1iRNGHv4cXuN4/E9Bx3RuUXn60e3Febc0iBnSH6h30xyCHwqgsDtEkUsQ3NneTyyXg0OZdPnuP5FQQpACCgDWJBvWir3skqyTyHUMyB4AgRkwErMEFWCH1ennTlaGtQsJzMMa8hxaaLYywVm7z2Yrx4UZ+1JCLdBgrG9AWudCQC4uBDIgOsC13DWBIcgQCCAgAPKIFtS/G0u7jd0tAeFk2d50uXxpfzgWjkMG9q3avn2ajvo2ZRcASMGH59UwUCVsCKEAdEq1YHUtsjxPOsMmmcNbvbrimSbtKjNCsrNp2QQyeNBncYem2fAl1nDFKM4RKiMEW2MMyTEnFwcV6ZIKYLbapm1a4oJCkTrb3fEFAIQAZ0GVbCdnVLxNOKg5jKbuxpq6mIBCpr0bpuLFJtZN06OKAF/BqfWi+OMHHUFv0eJekNMIsDAUKIGILA12qhSSsvr0zDLeGS0OAajlgLk4yUWCVt3Hcq7niX9TWn5LyNVMf5TBBi7WqrrFoiWkAz0rUG8PXOQIeQB/w19t8+sqYI04Xc7jtpbNl4sW29FjQlYS16UV5m8yo+H8vco6GNuy8Numrphx/zn37G0sm5w5bodcBLL1c67ghhLUyIB5I0Umb2QQUHJTfF11PXEFYBzUJmAYaCJ14RtYIcQqhFw+wJTDQLYg5EwIAg6TVG16GBBIgkpGh24/nxjjk8oDiFZ2KDMANrVkNVVINfnqazGQyhIoTXGTEQAz0CM8rQjPLZ6Ruk+7Fjm3GVej/IeTCQyd7w2ZxnE1QT1BJ280pfafFACwigZqaeSIY7D//sP3m6OKGzD3bMxx9GN48Gig7PEQUCAx0gBUr815cWqIEcyEBdSOIolHpyFeWZOtpS759sH5/slXVEY/iwLhHYzP1LLRLQDE2IRWcx3f31cVwVuDFI7h7tvXfqb+0NkpScvCSZgTMCamD16utRAOAClEcfEAALKua6LBRl5t6Je3BvtH8K1bVsitWV5QBBICAAjsEeHAAoMKMTI8/gAc8QqDN5ud/d6u+bN2/Vp8e7eiSWPG4m7cXlgak6lmGAhJESXAYdg1nBO7x9gnfexfePQCV6COnN1dG91UeMHD42y9XF9A/2y2bgr6LyTP8zS89aDAN6Xdy6j91jBEcvpmNdev14jN/+Bhp0YDrDxfGBvd0SQG1uIl7U0K3oKSPLae/3eVwYdAKSBHvH9u6e3Zc0Ho9ZCo4ltAIIDMFeOA97DSAgsCAwEYMgZIhlkIQAMCM4aj3Z8C+FfSsUjPCoqAAAAABJRU5ErkJggg==)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/N8Il1JcaQwLdbePjNnR8yA-VBkTPlmjVZAl17lebjV9hA) icon. To retrieve the data log file and empty the contents, confirm the operation from the Retrieve and Clear dialog.

After you confirm the operation, the Web server allows you to download the contents of the data log file. The Save File dialog lets you choose whether to save the data log. After your selection, the Web server empties the contents of the data log file without deleting the file. You cannot cancel the clearing of the data log from the Save File dialog. You can only cancel the operation from the initial confirmation of the Retrieve and Clear dialog.

You can only retrieve and clear a data log when "No" is listed in the "Active" column.

If an error message displays, or the Retrieve and Clear icon is not visible, you must then click the [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAIAAABvSEP3AAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH5gMOFR82s7ulQAAABANJREFUOI2NlF1PG0cUhs/M7rA2ttcyaxsLxS4fpRg7CNIWDCjUTZumogHUFilQKVLu8g9Q/kt7l5QbAheRUBJRcEIgFVDRBtMkNqVJSPgQIAwqu8Zez0cvTGziJlHP1Ugz550z533OoJ2dHQAAAIQQAAAIIeD9gRDCGAkhOD8+ik/sAcYIIfyO3HwIAJBlyWazWa3Wwp1yPl8IkUrpmQxzuWwWC3lXSYqiMCa2tlKp1LrTWe71qhhjIYQMABhjSlkyuZFIbAQC3lDolM/nkmWZUgqvH4kxUhQFY+nZs63p6fju7n5bW73X68AYM3asggBgZWV9eHjKVm658PUnPX2dNdU+mQCjLC9BCBECLy29GBmJrfy10XOxLRwOSBLKtyb/IgwA29upePxvztn+wWEux3t6OxsaqmQZTDOnKAql4teHS6Njs/H46umm6ubmWq/XZZq5Yl/yq4oKtbJS29rafPJkNZulupHp7+8Kh/xOp317+5+ZmeXhnyefJl+1ttb39Xac8ntMkxY8koaGho4tBoQxPjpiup7Z2dlbX981TVqhqZyJqalHP/04/vjxi6bm2sHBzyORBtVh5ZwX/S3wksnkdD29vLw2PBy7d++Pw8N0VZU7EgkpSlk8vrq5uReJBAd/OBeNNjlVG+f8pIlyYWWzKZpm1zTVYiH+gGd29s9k4uXk5CJjTJalSHvjpYFo19mwU7UJwUs4KKpwztNpkxC5s7NR05wIoZdr2/v7+wCi7sPqaLSlvb3R41FNk/0XpaKKEHkuRH4UGBWcCQCMkAQCDP0obWQoLa2iVOU1OGhvT5+Y+P3u3YX0UdYf8DnsNl0/Gh+f0zTV4bC63SoAFNw5Tiz2GaGyMnJ4mJmYWLx16+Hz568cqrX/+65r1y719bUfHBijow9isbhhmBiXzlqxFkVRMpnc3Fzi5s0H8fgqIZYzZ+q/udj2WVc4FArkcuzOnd/Gxma8XldHR9BiIYyxN1QQAgBkGNmFheT16xOLiytCiMZQoKc34vd7stlcXZ3v6tVuScKx2KMbN36RZNzW+pFFIYyzogrGmHORSKzdvj0/P//UMNL+gO/cF81dZ09rFappUknCtTW+K1fOSxKKxZZGRqatVqWlpVbCqHQCVLXc7XbY7dYyhfT2tn/3bWfA75EkxJiglGOMg0H/5ctfMsbn5hP37y+5PeoHfg1jxLmQ8w1HCNXUVHZ3f0oZp4xd+OrjpnA1wohSXqCJUggG/QMDUbvd6qqw0xwVIv9DiuIEYIwZY4aRFSDKrWWEECF4CRyShCllup4BQBYLIUQ69regkueFEBkAKGWMcXhbYIwJkTgXjLECNW9Qx7nIZnNvTT5xhmezpRe8/6/+v/EvPXIA4yoalWwAAAAASUVORK5CYII=)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/wuu7jJ3Aqn1deg1O8J7ffA-VBkTPlmjVZAl17lebjV9hA) icon in the Delete column to manually delete the file.

---

### User Files

The User Files page provides access to files on the SIMATIC memory card (external load memory).

The type of user file access you have depends on your user [privileges](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785). Any user with the "Read files" privilege can view the files and folders with the User Files page. If you have the "Write/delete files" privilege, you can also:

- Download a user file from your PLC to your computer
- Upload a user file from your computer to your PLC
- Delete a user file from your PLC

## Viewing user files

To view user files, click User Files from the main navigation page

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/1zbmhUYgT6HnT4Fm8Kq4Mw-VBkTPlmjVZAl17lebjV9hA/content?v=ee9cec351cbd8b60)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/1zbmhUYgT6HnT4Fm8Kq4Mw-VBkTPlmjVZAl17lebjV9hA)

The file list includes the file’s current size and the date of last modification. The list of files is populated from the "User Files" directory in the root of the SIMATIC memory card.

Note:

**User file management**

Keep no more than 1,000 user files on the SIMATIC memory card. If more files are present, the Web server only allows you to view the first 1,000 files. Files are displayed in ascending, case-insensitive, alphabetical order.

## User file list pagination

The user file list is paginated in increments of 50 items. A dropdown box lets you select the range of item you wish to see.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/m4n8Dah298J3yka~xesBJQ-VBkTPlmjVZAl17lebjV9hA)

## Downloading a user file

To download a user file, click a file in the list. Use Windows File Explorer to save the file to a folder you select.

## Deleting a user file

To delete a user file, click the X icon for the file and confirm the prompt.

## Uploading a user file

To upload a file from your programming device to the user files on your memory card, follow these steps:

1. Click Choose File.
2. From Windows File Explorer, select a file.

   The file must be less than 2 GB in size.

   The filename must consist only of these characters a-z A-Z 0-9 .\_- (){}[]$!=~ (space)
3. Click Upload file.

## Printing the User File list

You can print the list of the user files on your SIMATIC memory card by clicking the "Print" icon on your User Files Web page.

## Errors with user files

The User Files page displays an error message if an operation fails to complete successfully:

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/cDh5oUkL1SmLKBuF1RcCiw-VBkTPlmjVZAl17lebjV9hA)

The error message remains on the page until you refresh the User Files page.

Note:

**User files error message**

The Web server's auto-refresh functionality does not remove an error message from the User Files page.

The following conditions generate error messages on the User Files page:

| **Operation** | **Failure condition** | **Error message** |
| --- | --- | --- |
| Download user file | - File does not exist - Internal PLC error | Error while downloading the file |
| Download user file  Upload user file  Delete user file | - Insufficient permissions for requested operation - Invalid HTTP request method or action parameter | File operation not permitted |
| Download user file  Upload user file  Delete user file | - Invalid or missing HTTP referrer field | File operation not permitted - no referrer |
| Delete user file | - Memory card is write-protected | File operation not permitted |
| Download  Delete  Retrieve/Clear | - File does not exist - Internal PLC error | Error while deleting the file - memory card is write-protected |
| Upload user file | - File name missing or invalid - Internal PLC error | Error when uploading the file |
| Upload user file | - File name already exists on PLC | Error while uploading the file - name already exists |
| Upload user file | - SMC is full | Error while uploading the file - memory card is full |
| Upload user file | - Invalid file name | Error while uploading the file - invalid character in file name |
| Upload user file | - File is too large for SM file system | Error while uploading the file - file too big |
| Upload user file | - SMC is write-protected | Error while uploading the file - memory card is write-protected |

---

### Data Log UserFiles API

A Data Log User Files API feature is available for S7-1200 User Files and Data Logs. Refer to the [*S7-1500, ET200SP, ET200pro Web server manual*](https://support.industry.siemens.com/cs/us/en/view/59193560) for more information.

---

### File Browser

The File Browser page provides access to files in the internal load memory of the CPU or on the SIMATIC memory card (external load memory). The file browser page initially displays the root folder of the load memory, which contains the "Recipes" and "DataLogs" folders, but also displays any other folders that you might have created, if using a memory card.

The type of file access you have to the files and folders depends on your user [privileges](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785). Any user with "Read files" privileges can view the files and folders with the file browser. You cannot delete the Recipes or DataLogs folder regardless of your login privileges, but if you had made custom folders on the memory card, you can delete those folders if you have logged in as a user with "Write/delete files" privileges.

Click a folder to access the individual files in the folder.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/gHUQbKZDROoqPBejLHRFWA-VBkTPlmjVZAl17lebjV9hA/content?v=76735341145a6244)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/gHUQbKZDROoqPBejLHRFWA-VBkTPlmjVZAl17lebjV9hA)

## Recipe files

The recipe folder displays any recipe files that are present in load memory. Recipe files are also in CSV format, and you can open them in Microsoft Excel, or another program. You must have Write/delete [privileges](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785) in order to delete, modify and save, rename or upload recipe files.

## Uploading files and automatic page refresh

If you begin a file upload, the upload operation continues as long as you remain on the File Browser Web page. If you enabled automatic update to refresh the Web server pages every ten seconds, then whenever a page refresh occurs you see the incremental progress of the file upload operation. For example, if you are uploading a 2 MB file, you might see updates that show the file size in bytes at 2500, 5000, 10000, 15000, and 20000 as the file upload progresses.

If you navigate away from the File Browser page before the upload completes, the Web server deletes the incomplete file.

## Additional information

Note:

**File name conventions**

For the Web server to work with data log and recipe files, the characters in the file names must be from the ASCII character set with the exception of the characters \ / : \* ? " < > | and the space character.

If your files are not compliant with this naming convention, the Web server can have errors in operations such as file upload or deletion. In this case, you might need to use a card reader and the Windows File Explorer to rename files that were on external load memory.

For information on programming with the data log instructions, and [importing](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ofgDoR5EfsCG1KC3FI3nrQ?section=X00a94ffb0d39f618cbbf76ab8c37a518) and [exporting](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/OhXkfM4bQvMu1sBrt0mMcA?section=X748e2fceaa156a26df37cf78d936a4d7) recipes, see the [Recipes and Data logs](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/wN4rYJmmOvxg7MNBuNHfYA?section=X9408a52862e5181484246a710b19812b) chapter.

---

## User-defined Web pages


---

### Overview of user-defined Web pages

The S7-1200 Web server also provides the means for you to create your own application-specific HTML pages that incorporate data from the PLC.

Warning:

**Unauthorized access to the CPU through user-defined Web pages**

Unauthorized access to the CPU through user-defined Web pages can disrupt process operation. Coding of user-defined Web pages that is not secure introduces security vulnerabilities such as cross-site scripting (XSS), code injection, and others.

Protect your S7‑1200 CPU from unauthorized access by installing it in a secure fashion as outlined in the "Operational Guidelines" white paper found on the [Siemens Industrial Cybersecurity Web site](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Disruption of process operations can cause death, severe personal injury and/or property damage.

You create user-defined Web pages using the HTML editor of your choice and download them to the CPU where they are accessible from the standard Web page menu. This process involves several tasks:

- [Creating HTML pages with an HTML editor](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/b~asuu~AMmPQ_5qH0oWSqg?section=X2366120dafcbe77e666c13d3e142e39f)
- [Including AWP commands in HTML comments in the HTML code](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/~q9jluS9AvUsfTh_Xqdrwg?section=Xcd6bc549dcf126965d4e7e4a76174516):The AWP commands are a fixed set of commands that Siemens provides for accessing CPU information.
- [Configuring STEP 7 to read and process the HTML pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s7_eTegYUOQrpjL6XHouOA?section=Xe02f10865b52fd8c08edceb8507b84b8)
- [Generating blocks from the HTML pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s7_eTegYUOQrpjL6XHouOA?section=Xe02f10865b52fd8c08edceb8507b84b8)
- [Programming STEP 7 to control the use of the HTML pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/axkwnbW6OmPr8jiifBQdIQ?section=X6877d7f3022562c80e2844ed75aca5d8)
- [Compiling and downloading the blocks to the CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/vesoqOKaatLtqqgxAH6lHA?section=X978ec96628ce832c36e07e711a7b9cc8)
- [Accessing the user-defined Web pages from your PC](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/5ZeK8Xd840ctMarkYR8Ckg?section=X1359871aa57544332b07b932fe354cab)

This process is illustrated below:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/BKskzDRPLG~ap6QEePoabQ-VBkTPlmjVZAl17lebjV9hA/content?v=cef5897e7b6a24fc)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/BKskzDRPLG~ap6QEePoabQ-VBkTPlmjVZAl17lebjV9hA)

|  |  |
| --- | --- |
| ① | HTML files with embedded AWP commands |

---

### Creating HTML pages

You can use the software package of your choice to create your own HTML pages for use with the Web server. Be sure that your HTML code is compliant to the HTML standards of the W3C (World Wide Web Consortium). STEP 7 does not perform any verification of your HTML syntax.

You can use a software package that lets you design in WYSIWYG or design layout mode, but you need to be able to edit your HTML code in pure HTML form. Most Web authoring tools provide this type of editing; otherwise, you can always use a simple text editor to edit the HTML code. Include the following line in your HTML page to set the charset for the page to UTF-8:

**<meta http-equiv="content-type" content="text/html; charset=utf-8">**

Also be sure to save the file from the editor in UTF-8 character encoding.

You use STEP 7 to compile everything in your HTML pages into STEP 7 data blocks. These data blocks consist of one control data block that directs the display of the Web pages and one or more fragment data blocks that contain the compiled Web pages. Be aware that extensive sets of HTML pages, particularly those with lots of images, require a significant amount of [load memory space](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PkLEMaNdAAEiklPT_pFK6w?section=X4458d426be67e71f22bbf3a87345cfb0) for the fragment DBs. If the internal load memory of your CPU is not sufficient for your user-defined Web pages, use a [memory card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/M_966_mFNHNk6cgjPg_yKQ?section=Xd3c52365f0587b97b3dae91077ca2a13) to provide external load memory.

To program your HTML code to use data from the S7-1200, you include [AWP commands](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/~q9jluS9AvUsfTh_Xqdrwg?section=Xcd6bc549dcf126965d4e7e4a76174516) as HTML comments. When finished, save your HTML pages to your PC and note the folder path where you save them.

Note:

The file size limit for HTML files containing AWP commands is 64 kilobytes. You must keep your file size below this limit for STEP 7 to be able to successfully compile your pages.

Siemens recommends that all Web resource files (.ccc files, images, JavaScript files, and html files) are created with a size not exceeding 512 KB; otherwise, problems can occur when sending the file from the Web server to the browser. You can view the size of the respective Web resource file in the file explorer of the directory.

## Refreshing user-defined Web pages

User-defined Web pages do not automatically refresh. It is your choice whether to program the HTML to refresh the page or not. For pages that display PLC data, refreshing periodically keeps the data current. For HTML pages that serve as forms for data entry, refreshing can interfere with the user entering data. If you want your entire page to automatically refresh, you can add this line to your HTML header, where "10" is the number of seconds between refreshes:

**<meta http-equiv="Refresh" content="10">**

You can also use JavaScript or other HTML techniques to control page or data refreshing. For this, refer to documentation on HTML and JavaScript.

---

### AWP commands supported by the S7-1200 Web server


---

#### AWP commands supported by the S7-1200 web server

The S7-1200 Web server provides AWP commands that you embed in your user-defined Web pages as HTML comments for the following purposes:

- [Reading variables](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f~T8KkKGW6nCazIx7x9Mmw?section=X66b6d37f37f109f206061dfcd20fc466)
- [Writing variables](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/QBjzqZm~ICrraCcl613NGA?section=X1d8fe9814bcad8a7f42622dc34d16dfd)
- [Reading special variables](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/23L97pzp_AAWon3hg6clJQ?section=X3d1288c966bf398a2f69aa06e019d2d4)
- [Writing special variables](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/lF8_n~oQ737zbEe210M7jg?section=Xb49a0e7fb6ced190e581914656ec872e)
- [Defining enum types](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/rP3Y3VFxYOKSd2elWplBtg?section=X8ee10fb859f53de3475c8dcbc9163313)
- [Assigning variables to enum types](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Tp_qIxc27ApnQVTiN_o_xA?section=X02291812469d2816fe6510b996345803)
- [Creating fragment data blocks](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Iq9OqGiEr7o8kmQC9mTDFQ?section=Xc6b580efab886f310730ca5d372107c9)

## General syntax

Except for the command to read a variable, the AWP commands are of the following syntax:

**<!-- AWP\_** **<command name and parameters>** **-->**

You use the AWP commands in conjunction with typical HTML form commands to write to variables in the CPU.

The descriptions of the AWP commands in the following pages use the following conventions:

- Items enclosed in brackets [ ] are optional.
- Items enclosed in angle brackets < > are parameter values to be specified.
- Quotation marks are a literal part of the command. They must be present as indicated.
- Special characters in tag or data block names, depending on usage, [must be escaped or enclosed in quotation marks](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e).

Use a text editor or HTML editing mode to insert AWP commands into your pages.

Note:

**Expected syntax of AWP commands**

The space after "<!--" and the space before "-->" in the formulation of an AWP command are essential to proper compiling of the command. Omission of the space characters can cause the compiler to be unable to generate the proper code. The compiler does not display an error in this case.

## AWP command summary

The details for using each AWP command are in the topics to follow, but here is a brief summary of the commands:

**Reading variables**

**:=<****Varname****>:**

**Writing variables**

**<!-- AWP\_In\_Variable Name='<****Varname1****>' [Use='<****Varname2****>'] ... -->**

This AWP command merely declares the variable in the Name clause to be writable. Your HTML code performs writes to the variable by name from <input>, <select>, or other HTML statements within an HTML form.

**Reading special variables**

**<!-- AWP\_Out\_Variable Name='<****Type****>:<****Name****>' [Use='<****Varname****>'] -->**

**Writing special variables**

**<!-- AWP\_In\_Variable Name='<****Type****>:<****Name****>' [Use='<****Varname****>']-->**

**Defining enum types**

**<!-- AWP\_Enum\_Def Name='<****Enum type name****>' Values='<****Value****>, <****Value****>,... ' -->**

**Referencing enum types**

**<!-- AWP\_In\_Variable Name='<****Varname****>' Enum="<****Enum type name****>" -->**

**<!-- AWP\_Out\_Variable Name='<****Varname****>' Enum="<****Enum type name****>" -->**

**Creating fragments**

**<!-- AWP\_Start\_Fragment Name='<****Name****>' [Type=<****Type****>][ID=<****id****>] -->**

**Importing fragments**

**<!-- AWP\_Import\_Fragment Name='<****Name****>' -->**

---

#### Reading variables

User-defined Web pages can read variables (PLC tags) and data block tags from the CPU, provided that you have configured the tags to be accessible from an HMI.

## Syntax

**:=<Varname>:**

## Parameters

|  |  |
| --- | --- |
| <Varname> | The variable to be read, which can be a PLC tag name from your STEP 7 program, a data block tag, I/O, or addressable memory. For memory or I/O addresses or [alias names](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e), do not use quotation marks around the tag name. For PLC tags, use double quotation marks around the tag name. For data block tags, enclose the block name only in double quotation marks. The tag name is outside of the quotation marks. Note that you use the data block name and not a data block number. Reference array elements using array element syntax. |

## Examples

**:="****Conveyor\_speed****":**

**:="****My\_Data\_Block****".****flag1****:**

**:=I0.0:**

**:=MW100:**

**:="****My\_Data\_Block****".****Array\_Dim1****[0]:**

**:="****My\_Data\_Block****".****Array\_Dim2****[0,0]:**

## Example reading an aliased variable

**<!-- AWP\_Out\_Variable Name='****flag1****' Use='"****My\_Data\_Block".flag1****' -->:=****flag1****:**

Note:

Defining alias names for PLC tags and data block tags is described in the topic [Using an alias for a variable reference](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/fPVYuZLI9x432YilTD3ZtQ?section=Xad24415fe2d858f3c8191456bfbeae84).

If a tag name or data block name includes special characters, you must use additional quotation marks or escape characters as described in the topic [Handling tag names that contain special characters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e).

---

#### Writing variables

User-defined pages can write data to the CPU. This is accomplished by using an AWP command to identify a variable in the CPU to be writable from the HTML page. The variable must be specified by PLC tag name or data block tag name. You can declare multiple variable names in one statement. To write the data to the CPU, you use standard HTTP POST commands.

A typical usage is to design a form in your HTML page with text input fields or select list choices that correspond to writable CPU variables. As with all user-defined pages, you then generate the blocks from STEP 7 such that they are included in your STEP 7 program. When a user with privileges to modify variables subsequently accesses this page and types data into the input fields or selects a choice from a select list, the Web server converts the input to the appropriate data type for the variable, and writes the value to the variable in the CPU. Note that the name clause for HTML input fields and HTML select lists uses syntax typical for the name clause of the AWP\_In\_Variable command. Typically enclose the name in single quotation marks and if you reference a data block, enclose the data block name in double quotation marks.

For form management details, refer to documentation for HTML.

## Syntax

**<!-- AWP\_In\_Variable Name='<Varname1>' [Use='<Varname2>'] ... -->**

## Parameters

|  |  |
| --- | --- |
| <Varname1> | If no Use clause is provided, Varname1 is the variable to be written. It can be a PLC tag name from your STEP 7 program, a tag from a specific data block, or a data block name.  If a Use clause is provided, Varname1 is [an alternate name for the variable referenced in <Varname2>](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/fPVYuZLI9x432YilTD3ZtQ?section=Xad24415fe2d858f3c8191456bfbeae84). It is a local name within the HTML page. |
| <Varname2> | If a Use clause is provided, Varname2 is the variable to be written. It can be a PLC tag name from your STEP 7 program or a tag from a specific data block. |

For both Name clauses and Use clauses, the complete name must be enclosed in single quotation marks. Within the single quotes, use double quotation marks around a PLC tag and double quotation marks around a data block name. The data block name is within the double quotes but not the data block tag name. Note that for data block tags, you use the name of the block and not a data block number. Reference array elements using array element syntax.

If you use an AWP\_In\_Variable command to make a data block writable, then every tag in the data block is writable.

## Examples using HTML input field

**<!-- AWP\_In\_Variable Name='"****Target\_Level****"' -->**

**<form method="post">**

**<p>****Input Target Level:** **<input name='"****Target\_Level****"' type="text" /> </p>**

**</form>**

**<!-- AWP\_In\_Variable Name='"****Data\_block\_1****".****Braking****' -->**

**<form method="post">**

**<p>****Braking:** **<input name='"****Data\_block\_1****".****Braking****' type="text" /> %</p>**

**</form>**

**<!-- AWP\_In\_Variable Name='"****Data\_block\_1****".****Array\_Dim2****' -->**

**<form method="post">**

**<p>****Two-dimensional array value [2,1]:** **<input name='"****Data\_block\_1****".****Array\_Dim2[2,1]****' type="text" /> %</p>**

**</form>**

## Example using Use clause

**<!-- AWP\_In\_Variable Name='"****Braking****"' Use='"****Data\_block\_1****".****Braking****' -->**

**<form method="post">**

**<p>****Braking:** **<input name='"****Braking****"' type="text" /> %</p>**

**</form>**

## Example using writable data block

**<!-- AWP\_In\_Variable Name='"****Data\_block\_1****"' -->**

**<form method="post">**

**<p>****Braking:** **<input name='"****Data\_block\_1****".****Braking****' type="text" /> %**

**</p>**

**<p>****Turbine Speed:** **<input name='"****Data\_block\_1****".****TurbineSpeed****' size="10" value='"****Data\_block\_1****".****TurbineSpeed****' type="text" />**

**</p>**

**</form>**

## Example using HTML select list

**<!-- AWP\_In\_Variable Name='"****Data\_block\_1****".****ManualOverrideEnable****'-->**

**<form method="post">**

**<select name='"****Data\_block\_1****".****ManualOverrideEnable****'>**

**<option value=:"****Data\_block\_1****".****ManualOverrideEnable****:> </option>**

**<option value=1>****Yes****</option>**

**<option value=0>****No****</option>**

**</select><input type="submit" value="****Submit setting****" /></form>**

Note:

Only a user with the "Write process data through commands of the automation web page programming (AWP)" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785) can write data to the CPU. The Web server ignores the commands if the user does not have these privileges.

If a tag name or data block name includes special characters, you must use additional quotation marks or escape characters as described in the topic "[Handling tag names that contain special characters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e)".

---

#### Reading special variables

The Web server provides the ability to read values from the PLC to store in special variables in the HTTP response header. You might, for example, want to read a pathname from a PLC tag to redirect the URL to another location using the HEADER:Location special variable.

## Syntax

**<!-- AWP\_Out\_Variable Name='<****Type****>:<****Name****>' [Use='<****Varname****>'] -->**

## Parameters

|  |  |
| --- | --- |
| <Type> | The type of special variable, which is one of the following:  HEADER  COOKIE\_VALUE  COOKIE\_EXPIRES |
| <Name> | Refer to HTTP documentation for a list of all the names of HEADER variables. A few examples are listed below:  Status: response code  Location: path for redirection  Retry-After: how long service is expected to be unavailable to the requesting client  For types COOKIE\_VALUE and COOKIE\_EXPIRES, <Name> is the name of a specific cookie.  COOKIE\_VALUE:name: value of the named cookie  COOKIE\_EXPIRES:name: expiration time in seconds of named cookie  The Name clause must be enclosed in single or double quotation marks.  If no Use clause is specified, the special variable name corresponds to a PLC tag name. Enclose the complete Name clause within single quotation marks and the PLC tag in double quotation marks. The special variable name and PLC tag name must match exactly. |
| <Varname> | Name of the PLC tag or data block tag into which the variable is to be read  The Varname must be enclosed in single quotation marks. Within the single quotes, use double quotation marks around a PLC tag or data block name. The data block name is within the double quotes but not the data block tag name. Note that for data block tags, you use the name of the block and not a data block number. |

If a tag name or data block name includes special characters, you must use additional quotation marks or escape characters as described in the topic [Handling tag names that contain special characters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e).

## Example: Reading a special variable with no Use clause

**<!-- AWP\_Out\_Variable Name='"HEADER:Status"' -->**

In this example, the HTTP special variable "HEADER:Status" receives the value of the PLC tag "HEADER:Status". The name in the PLC tag table must match the name of the special variable exactly if no Use clause is specified.

## Example: Reading a special variable with a Use clause

**<!-- AWP\_Out\_Variable Name='HEADER:Status' Use='"****Status****"' -->**

In this example, the special variable "HEADER:Status" receives the value of the PLC tag "Status".

---

#### Writing special variables

The Web server provides the ability to write values to the CPU from special variables in the HTTP request header. For example, you can store information in STEP 7 about the cookie associated with a user-defined Web page, the user that is accessing a page, or header information. The Web server provides access to specific special variables that you can write to the CPU when logged in as a user with privileges to modify variables.

## Syntax

**<!-- AWP\_In\_Variable Name='<****Type****>:<****Name****>' [Use='<****Varname****>']-->**

## Parameters

|  |  |
| --- | --- |
| <Type> | The type of special variable and is one of the following:  HEADER  SERVER  COOKIE\_VALUE |
| <Name> | Specific variable within the types defined above, as shown in these examples:  HEADER:Accept: content types that are acceptable  HEADER:User-Agent: information about the user agent originating the request.  SERVER:current\_user\_id: id of the current user; 0 if no user logged in  SERVER:current\_user\_name: name of the current user  COOKIE\_VALUE:<name>: value of the named cookie  Enclose the Name clause in single quotation marks.  If no Use clause is specified, the special variable name corresponds to a PLC variable name. Enclose the complete Name clause within single quotation marks and the PLC tag in double quotation marks. The special variable name must match the PLC tag name exactly.  Refer to HTTP documentation for a list of all the names of HEADER variables. |
| <Varname> | The variable name in your STEP 7 program into which you want to write the special variable, which can be a PLC tag name, or a data block tag.  The Varname must be enclosed in single quotation marks. Within the single quotes, use double quotation marks around a PLC tag or data block name. The data block name is within the double quotes but not the data block tag name. Note that for data block tags, you use the name of the block and not a data block number. |

## Examples

**<!-- AWP\_In\_Variable Name='"SERVER:current\_user\_id"' -->**

In this example, the Web page writes the value of the HTTP special variable "SERVER:current\_user\_id" to the PLC tag named "SERVER:current\_user\_id ".

**<!-- AWP\_In\_Variable Name=SERVER:current\_user\_id' Use='"****my\_userid****"' -->**

In this example, the Web page writes the value of the HTTP special variable "SERVER:current\_user\_id" to the PLC tag named "my\_userid".

Note:

Only a user with the "Write process data through commands of the automation web page programming (AWP)" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785) can write data to the CPU. The Web server ignores the commands if the user does not have these privileges.

If a tag name or data block name includes special characters, you must use additional quotation marks or escape characters as described in the topic "[Handling tag names that contain special characters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e)".

---

#### Using an alias for a variable reference

You can use an alias in your user-defined Web page for an In\_Variable or an Out\_Variable. For example, you can use a different symbolic name in your HTML page than the one used in the CPU, or you can equate a variable in the CPU with a special variable. The AWP Use clause provides this capability.

## Syntax

**<-- AWP\_In\_Variable Name='<****Varname1****>' Use='<****Varname2****>' -->**

**<-- AWP\_Out\_Variable Name='<****Varname1****>' Use='<****Varname2****>' -->**

## Parameters

Table 1.

|  |  |
| --- | --- |
| <Varname1> | The alias name or special variable name  Varname1 must be enclosed in single or double quotation marks. |
| <Varname2> | Name of the PLC variable for which you want to assign an alias name. The variable can be a PLC tag, a data block tag, or a special variable. Varname2 must be enclosed in single quotation marks. Within the single quotes, use double quotation marks around a PLC tag, special variable, or data block name. The data block name is within the double quotes but not the data block tag name. Note that for data block tags, you use the name of the block and not a data block number. |

## Examples

**<-- AWP\_In\_Variable Name='SERVER:current\_user\_id' Use='"****Data\_Block\_10****".****server\_user****' -->**

In this example, the special variable SERVER:current\_user\_id is written to the tag "server\_user" in data block "Data\_Block\_10".

**<-- AWP\_Out\_Variable Name='****Weight****' Use='"****Data\_Block\_10****".****Tank\_data.Weight****' -->**

In this example, the value in data block structure member Data\_Block\_10.Tank\_data.Weight can be referenced simply by "Weight" throughout the rest of the user-defined Web page.

**<-- AWP\_Out\_Variable Name='****Weight****' Use='"****Raw\_Milk\_Tank\_Weight****"' -->**

In this example, the value in the PLC tag "Raw\_Milk\_Tank\_Weight" can be referenced simply by "Weight" throughout the rest of the user-defined Web page.

If a tag name or data block name includes special characters, you must use additional quotation marks or escape characters as described in the topic [Handling tag names that contain special characters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e).

---

#### Defining enum types

You can define enum types in your user-defined pages and assign the elements in an AWP command.

## Syntax

**<!-- AWP\_Enum\_Def Name='<****Enum type name****>' Values='<****Value****>, <****Value****>,... ' -->**

## Parameters

|  |  |
| --- | --- |
| <Enum type name> | Name of the enumerated type, enclosed in single or double quotation marks. |
| <Value> | <constant>:<name>  The constant indicates the numerical value for the enum type assignment. The total number is unbounded.  The name is the value assigned to the enum element. |

Note that the entire string of enum value assignments is enclosed in single quotation marks, and each individual enum type element assignment is enclosed in double quotation marks. The scope of an enum type definition is global for the user-defined Web pages. If you have set up your user-defined Web pages in [language folders](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/D9h~SOULZpSoCYx0EO_KbQ?section=Xf33dffb2ba1023020bdc9ac9e82394f3), the enum type definition is global for all pages in the language folder.

## Example

**<!-- AWP\_Enum\_Def Name='AlarmEnum' Values='0:"****No alarms****", 1:"****Tank is full****", 2:"Tank is empty"' -->**

---

#### Referencing CPU variables with an enum type

You can assign a variable in the CPU to an enum type. This variable can be used elsewhere in your user-defined Web page in a [read operation](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f~T8KkKGW6nCazIx7x9Mmw?section=X66b6d37f37f109f206061dfcd20fc466) or a [write operation](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/QBjzqZm~ICrraCcl613NGA?section=X1d8fe9814bcad8a7f42622dc34d16dfd). On a read operation, the Web server will replace the numerical value that is read from the CPU with the corresponding enum text value. On a write operation, the Web server will replace the text value with the integer value of the enumeration that corresponds to the text before writing the value to the CPU.

## Syntax

**<!-- AWP\_In\_Variable Name='<****Varname****>' Enum="<****EnumType****>" --><!-- AWP\_Out\_Variable Name='<****Varname****>' Enum="<****EnumType****>" -->**

## Parameters

|  |  |
| --- | --- |
| <Varname> | Name of PLC tag or data block tag to associate with the enum type, or the name of the [alias name for a PLC tag](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/fPVYuZLI9x432YilTD3ZtQ?section=Xad24415fe2d858f3c8191456bfbeae84) if declared.  Varname must be enclosed in single quotation marks. Within the single quotes, use double quotation marks around a PLC tag or data block name. Note that for data block tags, you use the name of the block and not a data block number. The data block name is within the double quotes but not the data block tag name. |
| <EnumType> | Name of the enumerated type, which must be enclosed in single or double quotation marks |

The scope of an enum type reference is the current fragment.

## Example usage in a variable read

**<!-- AWP\_Out\_Variable Name='"****Alarm****"' Enum="****AlarmEnum****" -->...<p>****The current value of "Alarm" is** **:="****Alarm****":</p>**

If the value of "Alarm" in the CPU is 2, the HTML page displays 'The current value of "Alarm" is Tank is empty' because the [enum type definition](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/rP3Y3VFxYOKSd2elWplBtg?section=X8ee10fb859f53de3475c8dcbc9163313) assigns the text string "Tank is empty" to the numerical value 2.

## Example usage in a variable write

**<!-- AWP\_Enum\_Def Name='****AlarmEnum****' Values='0:"****No alarms****", 1:"****Tank is full****", 2:"****Tank is empty****"' --><!-- AWP\_In\_Variable Name='"****Alarm****"' Enum='****AlarmEnum****' -->...**

**<form method="POST">**

**<p><input type="hidden" name='"****Alarm****"' value="****Tank is full****" /></p>**

**<p><input type="submit" value='****Set Tank is full****' /><p>**

**</form>**

Because the [enum type definition](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/rP3Y3VFxYOKSd2elWplBtg?section=X8ee10fb859f53de3475c8dcbc9163313) assigns "Tank is full" to the numerical value 1, the value 1 is written to the PLC tag named "Alarm" in the CPU.

Note that the Enum clause in the AWP\_In\_Variable declaration must correspond exactly to the Name clause in the AWP\_Enum\_Def declaration.

## Example usage in a variable write with use of an alias

**<!-- AWP\_Enum\_Def Name='****AlarmEnum****' Values='0:"****No alarms****", 1:"****Tank is full****", 2:"****Tank is empty****"' --><!-- AWP\_In\_Variable Name='"****Alarm****"' Enum='****AlarmEnum****' Use='"Data\_block\_4".****Motor1****.****Alarm****'-->...**

**<form method="POST">**

**<p><input type="hidden" name='"****Alarm****"' value="****Tank is full****" /></p>**

**<p><input type="submit" value='****Set Tank is full****' /><p>**

**</form>**

Because the [enum type definition](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/rP3Y3VFxYOKSd2elWplBtg?section=X8ee10fb859f53de3475c8dcbc9163313) assigns "Tank is full" to the numerical value 1, the value 1 is written to the alias "Alarm" which corresponds to the PLC tag named "Motor1.Alarm" in data block "Data\_Block\_4" in the CPU.

If a tag name or data block name includes special characters, you must use additional quotation marks or escape characters as described in the topic [Handling tag names that contain special characters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/GimSg4L3dVORPp5eIoh4uQ?section=Xf8aedf7421e263f6611ece5fe53d077e).

Note:

Previous releases required a separate AWP\_Enum\_Ref declaration to associate a variable with a defined enum type. STEP 7 and the S7-1200 support existing code with AWP\_Enum\_Ref declarations; however, this command is no longer needed.

---

#### Creating fragments

STEP 7 converts and stores user-defined Web pages as a control DB and fragment DBs when you click "Generate blocks" in the CPU Properties for the Web server. You can set up specific fragments for specific pages or for sections of specific pages. You can identify these fragments by a name and number with the "Start\_Fragment" AWP command. Everything in the page following the AWP\_Start\_Fragment command belongs to that fragment until another AWP\_Start\_Command is issued or until end of file is reached.

## Syntax

**<!--** **AWP\_Start\_Fragment Name=****'<Name>' [****Type=****<Type>][****ID=****<id>][****Mode=****<Mode>] -->**

## Parameters

Table 1.

|  |  |
| --- | --- |
| <Name> | Text string: name of fragment DB  Fragment names must begin with a letter or underscore and be comprised of letters, numeric digits, and underscores. The fragment name is a regular expression of the form:  [a-zA-Z\_][a-zA-Z\_0-9]\* |
| <Type> | "manual" or "automatic"  manual: The STEP 7 program must request this fragment and can respond accordingly. Operation of the fragment must be controlled with STEP 7 and the control DB variables.  automatic: The Web server processes the fragment automatically.  If you do not specify the type parameter, the default is "automatic". |
| <id> | Integer identification number. If you do not specify the ID parameter, the Web server assigns a number by default. For manual fragments, set the ID to a low number. The ID is the means by which the STEP 7 program controls a manual fragment. |
| <Mode> | "visible" or "hidden"  visible: Contents of the fragment will display on the user-defined Web page.  hidden: Contents of the fragment will not display on the user-defined Web page.  If you do not specify the type parameter, the default is "visible". |

## Manual fragments

If you create a manual fragment for a user-defined Web page or portion of a page, then your STEP 7 program must control when the fragment is sent. The STEP 7 program must set appropriate parameters in the control DB for a user-defined page under manual control and then call the WWW instruction with the control DB as modified. For understanding the structure of the control DB and how to manipulate individual pages and fragments, see the topic [Advanced user-defined Web page control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/jOJUoo3u5czXEoc06dCH7g?section=Xdbdac54bd0002b3dccd13c95de8678b3).

---

#### Importing fragments

You can create a named fragment from a portion of your HTML code and then import that fragment elsewhere in your set of user-defined Web pages. For example, consider a set of user-defined Web pages that has a start page and then several other HTML pages accessible from links on the start page. Suppose each of the separate pages is to display the company logo on the page. You could implement this by [creating a fragment](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Iq9OqGiEr7o8kmQC9mTDFQ?section=Xc6b580efab886f310730ca5d372107c9) that loads the image of the company logo. Each individual HTML page could then import this fragment to display the company logo. You use the AWP Import\_Fragment command for this purpose. The HTML code for the fragment only exists in one fragment, but you can import this fragment DB as many times as necessary in as many Web pages as you choose.

## Syntax

**<!-- AWP\_Import\_Fragment Name='<****Name**>' -->

## Parameters

|  |  |
| --- | --- |
| <Name> | Text string: name of the fragment DB to be imported |

## Example

Excerpt from HTML code that creates a fragment to display an image:

**<!-- AWP\_Start\_Fragment Name='****My\_company\_logo****' --><p><img src="****company\_logo.jpg****"></p>**

Excerpt from HTML code in another .html file that imports the fragment that displays the logo image:

**<!-- AWP\_Import\_Fragment Name='****My\_company\_logo****' -->**

Both .html files (the one that creates the fragment and the one that imports it) are in the folder structure that you define when you [configure the user-defined pages in STEP 7](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s7_eTegYUOQrpjL6XHouOA?section=Xe02f10865b52fd8c08edceb8507b84b8).

---

#### Combining definitions

When declaring variables for use in your user-defined Web pages, you can combine a variable declaration and an [alias for the variable](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/fPVYuZLI9x432YilTD3ZtQ?section=Xad24415fe2d858f3c8191456bfbeae84). You can also declare multiple In\_Variables in one statement and multiple Out\_Variables in one statement.

## Examples

**<!-- AWP\_In\_Variable Name='"****Level****"' Name='"****Weight****"' Name='"****Temp****"' -->**

**<!-- AWP\_Out\_Variable Name='HEADER:Status' Use='"****Status****"'         Name='HEADER:Location' Use="****Location****"         Name='COOKIE\_VALUE:name' Use="****my\_cookie****" -->**

**<!-- AWP\_In\_Variable Name='****Alarm****' Use='"****Data\_block\_10****".****Alarm****' -->**

---

#### Handling tag names that contain special characters

When specifying variable names in user-defined Web pages, you must take special care if tag names contain characters that have special meanings.

## Reading variables

You use the following syntax to [read a variable](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f~T8KkKGW6nCazIx7x9Mmw?section=X66b6d37f37f109f206061dfcd20fc466):

**:=<Varname>:**

The following rules apply to reading variables:

- For variable names from the PLC tag table, enclose the tag name in double quotation marks.
- For variable names that are data block tags, enclose the data block name in double quotation marks. The tag is outside of the quotation marks.
- For variable names that are direct I/O addresses, memory addresses, or alias names, do not use quotation marks around the read variable.
- For tag names or data block tag names that contain a backslash, precede the backslash with another backslash.
- If a tag name or data block tag name contains a colon, less than sign, greater than sign, or ampersand define an alias that has no special characters for the read variable, and read the variable using the alias. Precede colons in tag names in a Use clause with a backslash.

Table 1. Examples of Read variables

| **Data block name** | **Tag name** | **Read command** |
| --- | --- | --- |
| n/a | ABC:DEF | <!--AWP\_Out\_Variable Name='special\_tag' Use ='"ABC:DEF"' -->  :=special\_tag: |
| n/a | T\ | :="T\\": |
| n/a | A \B 'C :D | <!--AWP\_Out\_Variable Name='another\_special\_tag' Use='"A \\B \'C :D"' -->  :=another\_special\_tag: |
| n/a | a<b | <!--AWP\_Out\_Variable Name='a\_less\_than\_b' Use='"a<b"' -->  :=a\_less\_than\_b: |
| Data\_block\_1 | Tag\_1 | :="Data\_block\_1".Tag\_1: |
| Data\_block\_1 | ABC:DEF | <!-- AWP\_Out\_Variable Name='special\_tag' Use='"Data\_block\_1".ABC\:DEF'-->  :=special\_tag: |
| DB A' B C D$ E | Tag | :="DB A' B C D$ E".Tag: |
| DB:DB | Tag:Tag | <!--AWP\_Out\_Variable Name='my\_tag' Use ='"DB:DB".Tag\:Tag' -->  :=my\_tag: |

## Name and Use clauses

The AWP commands AWP\_In\_Variable, AWP\_Out\_Variable, AWP\_Enum\_Def, AWP\_Enum\_Ref, AWP\_Start\_Fragment and AWP\_Import\_Fragment have Name clauses. HTML form commands such as <input> and <select> also have name clauses. AWP\_In\_Variable and AWP\_Out\_Variable can additionally have Use clauses. Regardless of the command, the syntax for Name and Use clauses regarding the handling of special characters is the same:

- The text you provide for a Name or Use clause must be enclosed within single quotation marks. If the enclosed name is a PLC tag or Data block name, use single quotation marks for the full clause.
- Within a Name or Use clause, data block names and PLC tag names must be enclosed within double quotation marks.
- If a tag name or Data block name includes a single quote character or backslash, escape that character with a backslash. The backslash is the escape character in the AWP command compiler.

Table 2. Examples of Name clauses

| **Data block name** | **Tag name** | **Name clause options** |
| --- | --- | --- |
| n/a | ABC'DEF | Name='"ABC\'DEF"' |
| n/a | A \B 'C :D | Name='"A \\B \'C :D"' |
| Data\_block\_1 | Tag\_1 | Name='"Data\_block\_1".Tag\_1' |
| Data\_block\_1 | ABC'DEF | Name='"Data\_block\_1".ABC\'DEF' |
| Data\_block\_1 | A \B 'C :D | Name='"Data\_block\_1".A \\B \'C :D' |
| DB A' B C D$ E | Tag | Name='"DB A\' B C D$ E".Tag' |

Use clauses follow the same conventions as Name clauses.

Note:

Regardless of what characters you use in your HTML page, set the charset of the HTML page to UTF-8 and save it from the editor with UTF-8 character encoding.

---

### Configuring use of user-defined Web pages

To configure user-defined Web pages from STEP 7, follow these steps:

1. Select the CPU in the Device Configuration view.
2. Display the "Web server" properties in the inspector window for the CPU.
3. If not already selected, select the check box for "Activate Web server on this module".
4. Select "Permit access only with HTTPS" to ensure that the Web server uses encrypted communication and to increase the security of your Web-accessible CPU.
5. Enter or browse to the folder name on your PC where you saved the HTML default page (start page).
6. Enter the name of the default page.
7. Provide a name for your application (optional). The Web server uses the application name to further subcategorize or group web pages. When you provide an application name, the Web server creates an URL for your user-defined page in the following format: http[s]://ww.xx.yy.zz/awp/<application name>/<pagename>.html. If you do not provide an application name, the URL is http[s]://ww.xx.yy.zz/awp/<pagename>.html.

   Avoid special characters in the application name. Some characters can cause the Web server to be unable to display the user-defined pages.

   [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/0w4j2FJdxR4Ip3XvTP1rOA-VBkTPlmjVZAl17lebjV9hA/content?v=9b42bddae620b06d)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/0w4j2FJdxR4Ip3XvTP1rOA-VBkTPlmjVZAl17lebjV9hA)
8. In the Advanced section, enter filename extensions of files that include AWP commands. By default, STEP 7 analyzes files with .htm, .html, or .js extensions. If you have additional file extensions, append them. To save processing resources, do not enter file extensions if no files of that type include AWP commands.
9. Keep the default for the Web DB number, or enter a number of your choice. This is the DB number of the control DB that controls display of the Web pages.
10. Keep the default for the fragment DB start number, or enter a number of your choice. This is the first of the fragment DBs that contains the Web pages.

## Generating program blocks

When you click the "Generate blocks" button, STEP 7 generates data blocks from the HTML pages in the HTML source directory that you specified and a control data block for the operation of your Web pages. You can [set these attributes as needed for your application](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/axkwnbW6OmPr8jiifBQdIQ?section=X6877d7f3022562c80e2844ed75aca5d8). STEP 7 also generates a set of fragment data blocks to hold the representation of all of your HTML pages. When you generate the data blocks, STEP 7 updates the properties to display the control data block number, and the number of the first of the fragment data blocks. After you generate the data blocks, your user-defined Web pages are a part of your STEP 7 program. The blocks corresponding to these pages appear in the Web server folder, which is in the System blocks folder under Program blocks in the project navigation tree.

## Deleting program blocks

To delete data blocks that you have previously generated, click the "Delete data blocks" button. STEP 7 deletes the control data block and all of the fragment data blocks from your project that correspond to user-defined Web pages.

---

### Configuring the entry page

In the Device configuration of the CPU, you have the opportunity to designate a user-defined Web page to be the entry page when you access the Web server from either a PC or a mobile device. Otherwise, the entry page is the [Introduction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829) standard Web page.

To select a user-defined Web page to be the entry page, follow these steps:

1. Select the CPU in the Device configuration view.
2. In the inspector window, select "Web server" from the CPU properties and [enable the Web server](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zhgg0gJgOhxaX6BVSPQiIA?section=Xd1f721b46269feb9a0bd64cba8b230f3).
3. Select "Entry page" in the Web server properties.
4. Select "AWP1" from the drop-down list to configure the Web server to display a user-defined page upon access. (The other selection, "Start page", sets the Web server to display the standard Introduction Web page upon access.)

Users must have the "Open user-defined web pages" [privilege](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785). The STEP 7 program must include a call to the [WWW instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/axkwnbW6OmPr8jiifBQdIQ?section=X6877d7f3022562c80e2844ed75aca5d8).

After you have completed configuration and downloaded the project to the CPU, the Web server can use the "Default HTML page" that you selected when you [configured your user-defined Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s7_eTegYUOQrpjL6XHouOA?section=Xe02f10865b52fd8c08edceb8507b84b8) as the entry page.

Note:

The CPU must be in RUN mode to display a user-defined entry page.

---

### Programming the WWW instruction for user-defined web pages

Your STEP 7 user program must include and execute the WWW instruction in order for the user-defined Web pages to be accessible from the standard Web pages. The control data block is the input parameter to the WWW instruction and specifies the content of the pages as represented in the fragment data blocks, as well as state and control information. STEP 7 creates the control data block when you click the "Create blocks" button in the [configuration of user-defined Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s7_eTegYUOQrpjL6XHouOA?section=Xe02f10865b52fd8c08edceb8507b84b8).

## Programming the WWW instruction

The STEP 7 program must execute the WWW instruction for the user-defined Web pages to be accessible from the standard Web pages. You might want the user-defined Web pages available only under certain circumstances as dictated by your application requirements and preferences. In this case, your program logic can control when to call the WWW instruction.

Table 1. WWW instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **ret\_val := WWW(    ctrl\_db:=\_uint\_in\_);** | Provides access to user-defined Web pages from standard Web pages |

You must provide the control data block input parameter (CTRL\_DB) which corresponds to the integer DB number of the control DB. You can find this control DB block number (called Web DB Number) in the Web Server properties of the CPU after you create the blocks for the user-defined Web pages. Enter the integer DB number as the CTRL\_DB parameter of the WWW instruction. The return value (RET\_VAL) contains the function result. Note that the WWW instruction executes asynchronously and that the RET\_VAL output might have an initial value of 0 although an error can occur later. The program can check the state of the control DB to ensure that the application started successfully, or check RET\_VAL with a subsequent call to WWW.

Table 2. Return value

| **RET\_VAL** | **Description** |
| --- | --- |
| 0 | No error |
| 16#00yx | x: The request represented by the respective bit is in the waiting state:  x=1: request 0  x=2: request 1  x=4: request 2  x=8: request 3  The x values can be logically OR-ed to represent waiting states of multiple requests. If x = 6, for example, requests 1 and 2 are waiting.  y: 0: no error; 1: error exists and ["last\_error" has been set in the control DB](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/jOJUoo3u5czXEoc06dCH7g?section=Xdbdac54bd0002b3dccd13c95de8678b3) |
| 16#803a | The control DB is not loaded. |
| 16#8081 | The control DB is of the wrong type, format, or version. |
| 16#80C1 | No resources are available to initialize the web application. |

## Usage of the Control DB

STEP 7 creates the control data block when you click "Generate blocks" and displays the control DB number in the User-defined Web pages properties. You can find the control DB as well in the Program blocks folder in the project navigation tree.

Typically, your STEP 7 program uses the control DB directly as created by the "Generate blocks" process with no additional manipulation. However, the STEP 7 user program can set global commands in the control DB to deactivate the web server or to subsequently re-enable it. Also, for user-defined pages that you [create as manual fragment DBs](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s7_eTegYUOQrpjL6XHouOA?section=Xe02f10865b52fd8c08edceb8507b84b8), the STEP 7 user program must control the behavior of these pages through a request table in the control DB. For information on these advanced tasks, see the topic [Advanced user-defined Web page control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/jOJUoo3u5czXEoc06dCH7g?section=Xdbdac54bd0002b3dccd13c95de8678b3).

---

### Downloading the program blocks to the CPU

After you have generated the blocks for user-defined Web pages, they are part of your STEP 7 program just like any other program blocks. You follow the normal process to download the program blocks to the CPU. Note that you can only download user-defined Web page program blocks when the CPU is in STOP mode.

---

### Accessing the user-defined Web pages

You access your user-defined Web pages from the [standard Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Pk22gvnKDsZai3~SSAUQ8g?section=Xfc685e5b6a11fb2831d7fd61c3885d96). The standard Web pages display a link for "User-defined pages" on the left side navigation menu. The basic page navigation also provides a link to "User-defined pages". When you click the "User-defined pages" link, your Web browser goes to the page that provides a link to your default page. From within the user-defined pages, navigation is according to how you designed your specific pages.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/9wRrzcjmITHzXPN9daQS5w-VBkTPlmjVZAl17lebjV9hA/content?v=63bfd060068ae1a3)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/9wRrzcjmITHzXPN9daQS5w-VBkTPlmjVZAl17lebjV9hA)

Note:

You can also [define a user-defined page as the entry page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/gkY3~3V~j5L9s3vT2Dqc3w?section=X49d1982058a49937a91d62b575a1c58f) for the Web server.

---

### Constraints specific to user-defined Web pages

The [constraints for standard Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ehaPeqpl0WYqajaAiAqWeg?section=Xc066387d2c736f75df0974b4932a4a0d) also apply to user-defined Web pages. In addition, user-defined Web pages have some specific considerations.

## Load memory space

Your user-defined Web pages become data blocks when you click "Generate blocks", which require load memory space. If you have a memory card installed, you have up to the capacity of your memory card as external load memory space for the user-defined Web pages.

If you do not have a memory card installed, these blocks take up internal load memory space, which is limited according to your CPU model.

You can check the amount of load memory space that is used and the amount that is available from the Online and Diagnostic tools in STEP 7. You can also look at the properties for the individual blocks that STEP 7 generates from your user-defined Web pages and see the load memory consumption.

Note:

If you need to reduce the space required for your user-defined Web pages, reduce your use of images if applicable.

## Quotation marks in text strings

Avoid using text strings that contain embedded single or double quotation marks in data block tags that you use for any purpose in user-defined Web pages. Because HTML syntax often uses single quotes or double quotes as delimiters, quotation marks within text strings can break the display of user-defined Web pages.

For data block tags of type String that you use in user-defined Web pages, observe the following rules:

- Do not enter single or double quotation marks in the data block tag string value in STEP 7.
- Do not let the user program make assignments of strings containing quotes to these data block tags.

---

### Example of a user-defined web page


---

#### Web page for monitoring and controlling a wind turbine

As an example of a user-defined Web page, consider a Web page that is used to remotely monitor and control a wind turbine:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/qCbDutNmJs106ocqq~2pTg-VBkTPlmjVZAl17lebjV9hA/content?v=71eb1e87ba406b29)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/qCbDutNmJs106ocqq~2pTg-VBkTPlmjVZAl17lebjV9hA)

## Description

In this application, each wind turbine in a wind turbine farm is equipped with an S7-1200 for control of the turbine. Within the STEP 7 program, each wind turbine has a data block with data specific to that wind turbine.

The user-defined Web page provides remote turbine access from a PC. A user can connect to standard web pages of the CPU of a particular wind turbine and access the user-defined "Remote Wind Turbine Monitor" Web page to see the data for that turbine. A user with the "Write process data" privilege can also put the turbine in manual mode and control the variables for turbine speed, yaw, and pitch from the Web page.

A user with these privileges can also set a braking value regardless of whether the turbine is under manual or automatic control.

The STEP 7 program would check the Boolean values for overriding automatic control, and if set, would use the user-entered values for turbine speed, yaw, and pitch. Otherwise, the program would ignore these values.

## Files used

This user-defined Web page example consists of three files:

- **Wind\_turbine****.html**: This is the HTML page that implements the display shown above, using AWP commands to access controller data.
- **Wind\_turbine****.css**: This is the cascading style sheet that contains formatting styles for the HTML page. Use of a cascading style sheet is optional, but it can simplify the HTML page development.
- **Wind\_turbine.jpg**: This is the background image that the HTML page uses. Use of images in user-defined Web pages is, of course, optional, and does require additional space in the CPU.

These files are not provided with your installation, but are described as an example.

## Implementation

The HTML page uses AWP commands [to read values from the PLC](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f~T8KkKGW6nCazIx7x9Mmw?section=X66b6d37f37f109f206061dfcd20fc466) for the display fields and [to write values to the PLC](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/QBjzqZm~ICrraCcl613NGA?section=X1d8fe9814bcad8a7f42622dc34d16dfd) for data coming from user input. This page also uses AWP commands for [enum type definition](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/rP3Y3VFxYOKSd2elWplBtg?section=X8ee10fb859f53de3475c8dcbc9163313) and [reference](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Tp_qIxc27ApnQVTiN_o_xA?section=X02291812469d2816fe6510b996345803) for handling ON/OFF settings.

The first part of the page displays a header line that includes the wind turbine number.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Ww7FI0JSVMzdXzjT8Ml3VA-VBkTPlmjVZAl17lebjV9hA)

|  |  |
| --- | --- |
| The next part of the page displays atmospheric conditions at the wind turbine. I/O at the turbine site provide the wind speed, wind direction, and current temperature. | Figure 1. |
| Next, the page displays the power output of the turbine as read from the S7-1200. |  |
| The following sections allow for manual control of the turbine, overriding the normal automatic control by the S7-1200. These types are as follows: | |
| - Manual override: enables manual override of the turbine. The STEP 7 user program requires that the manual override setting be true before enabling the use of any of the manual settings for turbine speed, or yaw or pitch. |  |
| - Yaw override: enables manual override of the yaw setting, and a manual setting for the yaw. The STEP 7 user program requires that both manual override and yaw override be true in order to apply the yaw setting. |  |
| - Pitch override: enables manual override of the pitch of the blades. The STEP 7 user program requires that both manual override and pitch override be true in order to apply the blade pitch setting. |  |
| The HTML page includes a submit button to post the override settings to the controller. |  |
| The braking user input field provides a manual setting for a braking percentage. The STEP 7 user program does not require manual override to accept a braking value. |  |

In addition, the HTML page uses an AWP command to [write the special variable](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/lF8_n~oQ737zbEe210M7jg?section=Xb49a0e7fb6ced190e581914656ec872e) that contains the user ID of the user that is accessing the page to a tag in the PLC tag table.

---

#### Reading and displaying controller data

The "Remote Wind Turbine Monitor" HTML page uses numerous [AWP commands for reading data from the controller](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f~T8KkKGW6nCazIx7x9Mmw?section=X66b6d37f37f109f206061dfcd20fc466) and displaying it on the page. For example, consider the HTML code for displaying the power output as shown in this portion of the example Web page:

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANoAAAAPCAIAAAANjEYQAAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH2gceEzkypaSoRgAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAARLElEQVRogZ1aeWxcx3n/zbx5b29yeYu3LEqiZOqwLV+yY0s+4rOWk9SNHSNxktZO3SZoELR/pGnhAgUSNIjRoEWBpgbcoi5c1w58BT4Uy/IhWZZ8ShYpkeJ9ieRyyeWeb3ffezPTP957u2+XpKT4A0HwmPm+b775fecsuecfDwMSMGATIZDM/lEBFBAA5QUEoPYyGAAEIOy/2mvsXQoDE0KY0oICAqpCBcDBOUwAgAYK0NJ2mygBCMAUGFwAHOCgACGACm6vEQAngAopARPE1kdCApKAgBBIFZwAgJSgBFIAlqMxGCqIC3CAKaAqKCABC64kCxAAkVAlLALpsgQhIK58AJKAA0ziEokACiABQSBVSAMSkIByCXstx75wTU4ACEi+lhSPRrZ1IJ2rKxEDqAIIGJegfvmObQVEhYgLECewGCDh4xffwlxZPld3XoImBzg0wDW9rY59+NLJKCBU7xppy6SKrbgH6SWZRnmvzUdQCM3mYnAApqO48DKggAYwCcHBOQCozippSmEwKGASQgAMgoObULSSGgCvVoRAgghpUUINRYOFEhZLJCUMDk0BJQBQ5JBEwmc4yAAFUcFE2T4XJtuZHRtKwABx77nCPsCaN2fflXC2UAGVYA3Ztt9JF76AAEwCSPhdmAYjoWu2b2DL5w+PFQCAkI5NbTe0+4XF+/snz2UAAD7fVVtbNjeo+WT2k6FYogAJmOHI3X2NER9NzsePjqfzZYMpPVuadzRpg/1TwxkAaGxqvG57rWZkB4bzm/qajPnz744XIMmOnZ2X15GJ4cWTC3nL57+6t7mdpg+dSuqeI65HtNrR1l7lGkTY34QBA6CAepGNX4ooqAoqAGn7i3O1SoXv20GImJ7bXn0KqoAoqyBYvYiAuDwYhSm8oBWAAcIuKU7YWOSojlF/KLnbhYSxZojyALG8SbixAQClvVds+Yv9bec/W7HhGOzu/un9Wy6LqoKLoRblqbfHRnJ0x1W9f7WvtSmoGIVCX4349+PxtBo+sH/7d6+q9zOqp9tbXv/4fwYLrgR167bOB3eEX5iZGs5A8wUfuHfnHZvIR7//YqAmfNt1vXVj+ruj8whG7t23+eZmtd9vDi/lizWhW/du3pEZfeNUEgrAwQABsO6OSNDhywGOYn4wbgJsLecFUL4h1wCQpJx5pZOB1jJlFTwIgbTjq/As0gDuMaq9R/UFfXXEWNQ5KPWkb/eChB1uLXDLjTqOGuGasL+YXSqu1oeAE0gCy645iKxSm0Ao4MQRYTqp1uuiEkRcEhxLiUVcZOFqMK1BAiiJZdX/qtBIAeVlw0dqgnffffXD2wLlC1R839zfXZeP//z/+he7Lv/V7a1fGYsvTtCHbmozJs89dvD8ntuueXRv55GB1GJL01276s5+cOKfBugP7t911/6ut88Nz686Dgv4vnbg6q+2mu+9fvY/P01kg7Vji9mbW8KtQLwx2qWJyVi2rTXo02hTfU13ozo+lDThGIcBBhD+4ff39HlNtxJ/8ndD702vnYMooHE7A0oQWx3KiSKI4HYhs2ZIJZ7A4Lg1haKBAFQAJoR0sejNYfZfEI6E7r5l62WxwSc/TUNqVYxBCCgFAFIdMVrbGr+27/KVD4/8dsrFMHG/EwaFgdsZjzIwsyr1EYDAKvGjgLT1KTpSFKxVu61BpYphXbJ9h0KxzeP+WkEU1Z6+Kt1TAg0wbVkUdkUNaV8K3XHl5pvCyTdPJ6/Z1uFsCIW7ojSxmFmI85ixsnBPU2uNL1gfbA8bI7N6OiOnppKp3fXdEVZoiNT59Q9GC7k0mUjk9/REOnyYz1dq6PPv3bvtwEb53ruDz32eyHIgbyzminJDQ09kJNISZCJ74rPMV/YEa1UWrAlFfPrR0XKcKHvW4vTscx/PLRZIeEPLI9e3PXRD68zC9Fh13VeyigoAhENxMrQiFArKwcsZ/gJhQLoGcvhJQFavp56VQG00sndLnZ7wcqaACgoQAVLqVJyLcFol0I6ulus7Ar8H7AgsiacYF2AUkkoupJNHK6+fEEIIEZarGYUCxquORkqy1iXbXvJS4AiopTOISjiWDAIXhetHZYay7xEKxmFKAOLs6fFf9xdF/Ya+Ehz9vnpKTEsUTcg8L0BrjPoCGX8U0ihSwZlVECaC7c1sKuAPQmSLEhxFSxIl3BIFvHCkdMv2rjv7WmrUIoWVMwEYsPhELM97Grvag4GmMCuk+xdy29XGKxvVufpQ7XLmZIZ71XaomNOHppamdarMiZ3b6m+sqW0Oi7G0euMVm793R0cz5Ep88X9fG3xv0Xr0T2+5IjX7qzfG9VDz4w/s7MtPPPpfo2ZbyxMHNufHTv/r8WzPtdt+dn0LgPjoxN+/PrmQ8z3ynV231olMQe2oyT/51MfH0k5rGI1GH/l6761NAaD4+ZFz//FJbKGIPfuvfGIXeebQqRdH9DsP3PCX9Zm/fXXmvvu3bw1A7rvu1x2jLw8oD95+GVmaS0bbt4fluVNnfvnBcqKIR7617xva3N+8NDRDQo8d2H1TfuonxwoP7e1q8OFb376l8/CZp0fYz/98+9LHg/98dH5ZwAWRAyVBRPn6JQAiQaR00UYAEA4CKiCY3UIQCdh99/qI9MYvbyCTq5ZJCSYhiBNzK+IgASEEAlKsj0EJSEjpep0sua4kjveT1Eo2DWysrxDsauXU+oSwUo9ZPhXxFNFOBiKVNRtUTb2+r/lI/7TR037j3q2DsS/enjSEFBMLSZ03dG9sCNT5ZkdiA1nlZl3t7VSV5uDS4uKyaZVcq+x9kYb6u67r+eaNm7/91e7rG/wr8cXJrNmzo/NHd2zQJ+ZePT4RD7R+90DvtY3ks/GV+uZAS1BGouH2eqq21u/U1I7mcF0IQ2PFzTt7f3h17fHjky9+Npdv63z8xnANE1ShTYFAdmX5xWMTX2Sdo0drIw/f3buv1jx4fPrwaHHbjbseubqhBqCUMoVSQkAIpZQpRJL8wMhiwkJ8eu6dsytpQhijdfU1S+emD03rfbt6vr415CNEoZQphCgqUVSFUkZJJpM7O5fOc3nmzNSHC7mckT14Yur9qWKe+0AVUMOCwSkHAxi44glegoH7wBVw4dyIZOA+CAEYYKZtOVWAcYCvi0UG+Nx7tucX9tfqFpJRgMEiMAADIAzMs4hKaJwyzhyQSTcqewEhAA4pYFCYzJ0ocUinuZS2DmpVj5kvLgupMmhqAX7qgxFfyRVSehJE8wlKTcVHGfT5Raug53XQkAaAaAqRPLuQqDiCsKwTHw4++9bgbz6Ooy56767W2oAPipqayUxZomNj4+56NjVV1JP6+LLe1h3tqWOzC/miJwOXTxxtbry/udH+eXl85F/eOz+vhB7b1cSXl146dPbokrUrGfjxH0WvavS/NBmb271xZ532UVMwM7Wcq/W3tGhqQyhsJj+Jsz27w1GNtbXVhhSlVqOBtqYObRZANp09dHzwnYXylW9oa97Tyc4cOfP0B1klVEsf3t7X09jxSXr1pUppnRqav21HS35i5o3Tyc6dTRBycmjiN4cTojbd96NtG+sDEUVfvTGdyp6eSd7cFT51avzoLAC8/H4aUEEuZdB3cbq0Ac+XoSqEC8AAB71oH+Surqg67GLBQa5VpXYudz4tttbUNDeqsrOu1TA/yxT1hDWf07rbgqHwSmdXbTSvT6bNzEo2VWzt3eTz5+jGhgDNzp8veBmBW3xkYnnJRGpg7J0d9fft2HTfeOyZswUUc7Esua6tUeYTzy1Z1OIr6Xy0t6dB5N9Y0gueIFCG48zg8C8Pjk3bdyoll0CYhTSa1fXZhCWAlZRexIamqJIeTA3H2ab24HKDPzYWS3a3bdpSE20OLo+Ozij0zohKOaApfshYPJNNEsUPAIZlVUgGmKb5FGNshhsAcsWUKfxasCZUUWCpToPiDQPELjbn4rmsgJIxcmA1QZ/mcXlKoFQlEu/uSxzgVpO1uuldj5Et22643Jn+pVBFPVjFXF5IIAB3jitdLJegW6qXGaSAlFBKYGUACi8cm7n2QM/f/eAOIeXE0MSxqXQyq7xwbOGvb+p96ifbuWl++tHYQNZITccPnW1++Oa9z+8nhp5/683p+DqKmNncW0dn+v645+6bLjs+NjSiG8eGkw90txXmchOmAOSp6Wx+T2t93phOF72+wbwPAlxI7k5ZQQFuJHReV1+zrcM3eb7Y1VkXMbIn4oahy7ll/er2tt0RZWggPqlFH+/bkCHK2JmCZYqUbpmG8fwrnxyztFt7m1QjNZXGHsCy8vnKUUtR17Nm6xWX14am8mpzuD2gppdT8xk0A6DwM6KSQG9LEEYSUOwuwx/QCBS7iunuiDb3x4rNoQZYU5liwY75KgsRUhsIbKj1QQekYr+o+H2qJygI99llfXLaHQKxTk9M16ivSv8pdf68JLXKO1bhioAq0ACLr+Z4ASr1VYpnYuD9Iy+NwNxxLLCUTL91YpTP5+0tmYnJX7xu7evwc8s6eXp8KAOAn/p86N8Kqd56NZfKHB+MpSRQyLz4/qCVaKrVaGI29sGwt4uxxkbmXklr55zcJscnZ599k2+uJZEIgS5nhuee1/TE+ViqIACk5hO/Ozau6NnBWAUmGKCWIzv1nAqAmX9zIPHgfZ1/cu+eGzLmhg2Nxuz45/E8DDo+l+W97R355DuJTD/PRW7oDq0sP7tQtHR+ciJ5y2Ud3//GVXcJdUtz8OTx4++vY8mFWGLgfPcduzf9Q/0GJRTorlUPHYmdt5BeTMPfeusNO7fvoj1RYBGAIkyZL6K3r/fH5Hz/CgglG3s3/SzaaoaDNdn86YVMisuxxTTa6v/s3p1F5tvozFGVnA4h6f79VyiRsZcnyffu6k4NTf72dCJ9STfuDTgAQCQYh0lXwWstqsBiVXWwFogpIMG488Ql3KRwQUW9yKui0iPQqkfI5ErqtQ9SHiZiamTmmRGnP3OnrIWPvpj4qIpnJvXqhykiwewnx3IDZw0PzQ4PeVYWCydOTpxwf8vHFp+JLZb/m069ctSjgEvKllu+A9AtPZHsfOLz2YzOFQ0ah7TNrceX3x83WrsiNQqZn5l8+uDoqE6kRLyAtqiWXYl/PJhc0klnZ2RyNHZkLJmxRDy2PFbUtjf5GJGjA/1Pfpgyoba1RrRc7tR4MmGPnSUhILxonhxYTtYENtZoUuTffav/v0cKQsrCciIdbmj2E+gLrw2bIVM/Np5eTHNDodGgyvO5BV25vKs2PjbezyMNxDz4Tv/Lo4aQWFnJ0lAkqmF+bqF/0RKZ5OGxXCJlRerUiErTS8nBFeXabQ3mUmogli/K9QFlt40gRJYaB0FcdCgAJyj9SqoH56AEilJ+DCCEEBAHGc4aQiQpcyg/ZVMJ6UzOHGbliY0EsVbXvO7ch9DSOzYph97S0M1TSlZNKt1TEEgF4B4u6xqHSqcUlYC30Xd2kYt9VdmL2O9ICgByzy9ed//DAFb22nJVyb21rwZNCmkKs7RGgyYhSwNkxsEkQMCVkq9VTK3LIlbHjLIsd9fqxEV4z85NP739svlPP33iw+x6a6CYgPMargES3IQJaCDUFcrXbUUEICpe60tn4ASmrEzHBKZS3qjYOYZ63501TqSpmHaQZQCr+iRASRvqxY27phya19hVIgZQMBNMXuBczh27soTTaFOAC5i8/Axnn2JtLhKEQ5XOk6dZxZnAZNXrnWqhBETvQytzE4D7KrOK1ncNCuq8pLlryn9ZxUUBA2CurrpKzzOXkO/W1EF1PtKwluZyDbauV6hfUqRXuvQWN5UkAAEOSAKl4jMQ7pVdtJ0R3sT6h3Xt1kXm4mUVym+qLrqJ3e14noTXn1wBBJJC8Goj8At8ymd1RFRcmFbq/f+bvhNGaBrOeQAAAABJRU5ErkJggg==)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/5xN6EFRTCv6RIZWTtqnXjA-VBkTPlmjVZAl17lebjV9hA)

## Example HTML code

The following excerpt from the "Remote Wind Turbine Monitor" HTML page displays the text "Power Output:" in the left cell of a table row and reads the variable for the power output and displays it in the right cell of the table row along with the text abbreviation for kilowatts, kW.

The AWP command :="Data\_block\_1".PowerOutput: performs the read operation. Note that data blocks are referenced by name, not by data block number (that is, "Data\_block\_1" and not "DB1").

<tr style="height:2%;"><td><p>Power output:</p></td><td><p style="margin-bottom:5px;"> :="Data\_block\_1".PowerOutput: kW</p></td></tr>

---

#### Using an enum type

The "Remote Wind Turbine Monitor" HTML page uses enum types for the three instances where HTML page displays "ON" or "OFF" for a Boolean value, and for where the user sets a Boolean value. The enum type for "ON" results in a value of 1, and the enum type for "OFF" results in a value of 0. For example, consider the HTML code for reading and writing the Manual Override Enable setting in "Data\_block\_1".ManualOverrideEnable value using an enum type:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/AXeA~ggYgRHi1Fc2LVxa5w-VBkTPlmjVZAl17lebjV9hA/content?v=c5061eb2b80f2855)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/AXeA~ggYgRHi1Fc2LVxa5w-VBkTPlmjVZAl17lebjV9hA)

## Example HTML code

The following excerpts from the "Remote Wind Turbine Monitor" HTML page show how to declare an enum type called "OverrideStatus" with values of "Off" and "On" for 0 and 1, and then setting an enum type reference to OverrideStatus for the ManualOverrideEnable Boolean tag in the data block named "Data\_block\_1".

<!-- AWP\_In\_Variable Name='"Data\_block\_1".ManualOverrideEnable' Enum="OverrideStatus" --><!-- AWP\_Enum\_Def Name="OverrideStatus" Values='0:"Off",1:"On"' -->

Where the HTML page includes a display field in a table cell for the current state of ManualOverrideEnable, it uses just a normal read variable command, but with the use of the previously declared and referenced enum type, the page displays "Off" or "On" rather than 0 or 1.

<td style="width:24%; border-top-style: Solid; border-top-width: 2px; border-top-color: #ffffff;"><p>Manual override: :="Data\_block\_1".ManualOverrideEnable:</p></td>

The HTML page includes a drop-down select list for the user to change the value of ManualOverrideEnable. The select list uses the text "Yes" and "No" to display in the select lists. With the use of the enum type, "Yes" is correlated to the value "On" of the enum type, and "No" is correlated to the value "Off". The empty selection leaves the value of ManualOverrideEnable as it is.

<select name='"Data\_block\_1".ManualOverrideEnable'><option value=':"Data\_block\_1".ManualOverrideEnable:'> </option><option value="On">Yes</option><option selected value="Off">No</option></select>

The select list is included within a form on the HTML page. When the user clicks the submit button, the page posts the form, which writes a value of "1" to the Boolean ManualOverrideEnable in Data\_block\_1 if the user had selected "Yes", or "0" if the user had selected "No".

---

#### Writing user input to the controller

The "Remote Wind Turbine Monitor" HTML page includes several [AWP commands for writing data to the controller](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/QBjzqZm~ICrraCcl613NGA?section=X1d8fe9814bcad8a7f42622dc34d16dfd). The HTML page declares AWP\_In\_Variables for Boolean variables so that a user with the "Write process data" privilege can put the wind turbine under manual control and enable manual override for the turbine speed, yaw override, and/or blade pitch override. The page also uses AWP\_In\_Variables to allow a user with these privileges to subsequently set floating-point values for the turbine speed, yaw, pitch, and braking percentage. The page uses an HTTP form post command to write the AWP\_In\_Variables to the controller.

For example, consider the HTML code for manually setting the braking value:

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/yFHD2pPWqAh3mMHFMnVwQw-VBkTPlmjVZAl17lebjV9hA)

## Example HTML code

The following excerpt from the "Remote Wind Turbine Monitor" HTML page first declares an AWP\_In\_Variable for "Data\_block\_1" that enables the HTML page to write to any tags in the data block "Data\_block\_1". The page displays the text "Braking:" in the left cell of a table row. In the right cell of the table row is the field that accepts user input for the "Braking" tag of "Data\_block\_1". This user input value is within an HTML form that uses the HTTP method "POST" to post the entered text data to the CPU. The page then reads the actual braking value from the controller and displays it in the data entry field.

A user with the "Write process data" privilege can use this page to write a braking value to the data block in the CPU that controls braking.

<!-- AWP\_In\_Variable Name='"Data\_block\_1"' -->

...

<tr style="vertical-align: top; height: 2%;"><td style="width: 22%;"><p>Braking:</p></td>

<td><form method="POST"><p><input name='"Data\_block\_1".Braking' size="10" type="text"> %</p></form></td>

</tr>

Note:

Note that if a user-defined page has a data entry field for a writable data block tag that is a string data type, the user must enclose the string in single quotation marks when entering the string value in the field.

Note:

Note that if you declare an entire data block in an AWP\_In\_Variable declaration such as <!-- AWP\_In\_Variable Name='"Data\_block\_1"' -->, then every tag within that data block can be written from the user-defined Web page. Use this when you intend for all of the tags in a data block to be writable. Otherwise, if you only want specific data block tags to be writable from the user-defined Web page, declare it specifically with a declaration such as <!-- AWP\_In\_Variable Name='"Data\_block\_1".Braking' -->

---

#### Writing a special variable

The "Remote Wind Turbine Monitor" Web page writes the special variable SERVER:current\_user\_id to a PLC tag in the CPU, providing that the user has the "Write process data" privilege. In this case, the PLC tag value contains the user ID of the user who is accessing the "Remote Wind Turbine Monitor" Web page.

The Web page writes the special variable to the PLC and requires no user interface.

## Example HTML code

**<!-- AWP\_In\_Variable Name="SERVER:current\_user\_id" Use="****User\_ID****"-->**

---

#### Reference: HTML listing of remote wind turbine monitor Web page

## Wind\_turbine.html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"><!--

This test program simulates a Web page to monitor and control a Wind Turbine

Required PLC tags and Data Block Tags in STEP 7:

PLC Tag:

User\_ID: Int

Data Blocks:

Data\_block\_1

Tags in Data\_Block\_1:

TurbineNumber: Int

WindSpeed: Real

WindDirection: Real

Temperature: Real

PowerOutput: Real

ManualOverrideEnable: Bool

TurbineSpeed: Real

YawOverride: Bool

Yaw: Real

PitchOverride: Bool

Pitch: Real

Braking: Real

The user-defined Web page displays current values for the PLC data, and provides a select list to set the three Booleans using an enumerated type assignment. The "Submit" button posts the selected Boolean values as well as the data entry fields for TurbineSpeed, Yaw, and Pitch. The value for Braking can be set without use of the "Submit" button.

No actual STEP 7 program is required to use this page. Theoretically, the STEP 7 program would only act on the values of TurbineSpeed, Yaw, and Pitch, if the associated Booleans were set. The only STEP 7 requirement is to call the WWW instruction with the DB number of the generated data blocks for this page.

-->

<!-- AWP\_In\_Variable Name='"Data\_block\_1"' -->

<!-- AWP\_In\_Variable Name='"Data\_block\_1".ManualOverrideEnable' Enum="OverrideStatus" -->

<!-- AWP\_In\_Variable Name='"Data\_block\_1".PitchOverride' Enum="OverrideStatus" -->

<!-- AWP\_In\_Variable Name='"Data\_block\_1".YawOverride' Enum="OverrideStatus" -->

<!-- AWP\_In\_Variable Name="SERVER:current\_user\_id" Use="User\_ID"-->

<!-- AWP\_Enum\_Def Name="OverrideStatus" Values='0:"Off",1:"On"' -->

<html>

<head>

<meta http-equiv="content-type" content="text/html; charset=utf-8">

<link rel="stylesheet" href="Wind\_turbine.css">

<title>Remote Wind Turbine Monitor</title>

</head>

<body>

<table cellpadding="0" cellspacing="2">

<tr style="height: 2%;">

<td colspan="2">

<h2>Remote Wind Turbine Monitor: Turbine #:="Data\_block\_1".TurbineNumber:</h2>

</td>

<tr style="height: 2%;"><td style="width: 25%;"><p>Wind speed:</p></td>

<td><p> :="Data\_block\_1".WindSpeed: km/h</p></td>

</tr>

<tr style="height: 2%;">

<td style="width: 25%;"><p>Wind direction:</p></td>

<td><p> :="Data\_block\_1".WindDirection: deg.</p></td>

</tr>

<tr style="height: 2%;"><td style="width: 25%;"><p>Temperature:</p></td>

<td><p> :="Data\_block\_1".Temperature: deg. C</p></td>

</tr>

<tr style="height: 2%;">

<td style="width: 25%;"><p>Power output:</p></td>

<td><p style="margin-bottom:5px;"> :="Data\_block\_1".PowerOutput: kW</p>

</td>

</tr>

<form method="POST" action="">

<tr style="height: 2%;" >

<td style="width=25%; border-top-style: Solid; border-top-width: 2px; border-top-color: #ffffff;">

<p>Manual override: :="Data\_block\_1".ManualOverrideEnable:</p>

</td>

<td class="Text">Set:

<select name='"Data\_block\_1".ManualOverrideEnable'>

<option value=':="Data\_block\_1".ManualOverrideEnable:'> </option>

<option value="On">Yes</option>

<option value="Off">No</option>

</select>

</td>

</tr>

<tr style="vertical-align: top; height: 2%;"><td style="width: 25%;"><p>Turbine speed:</p></td>

<td>

<p style="margin-bottom:5px;"><input name='"Data\_block\_1".TurbineSpeed' size="10" value=':="Data\_block\_1".TurbineSpeed:' type="text"> RPM</p>

</td>

</tr>

<tr style="vertical-align: top; height: 2%;">

<td style="width: 25%;">

<p>Yaw override: :="Data\_block\_1".YawOverride: </p>

</td>

<td class="Text">Set:

<select name='"Data\_block\_1".YawOverride'>

<option value=':="Data\_block\_1".YawOverride:'> </option>

<option value="On">Yes</option>

<option value="Off">No</option>

</select>

</td>

</tr>

<tr style="vertical-align: top; height: 2%;">

<td style="width: 25%;">

<p>Turbine yaw:</p>

</td>

<td>

<p style="margin-bottom:5px;"><input name='"Data\_block\_1".Yaw' size="10" value=':="Data\_block\_1".Yaw:' type="text"> deg.</p>

</td>

</tr>

<tr style="vertical-align: top; height: 2%;">

<td style="width: 25%;">

<p>Pitch override: :="Data\_block\_1".PitchOverride: </p>

</td>

<td class="Text">Set:

<select name='"Data\_block\_1".PitchOverride'>

<option value=':="Data\_block\_1".PitchOverride:'> </option>

<option value="On">Yes</option>

<option value="Off">No</option>

</select>

</td>

</tr>

<tr style="vertical-align: top; height: 2%;">

<td style="width=25%; border-bottom-style: Solid; border-bottom-width: 2px; border-bottom-color: #ffffff;">

<p>Blade pitch:</p>

</td>

<td>

<p style="margin-bottom:5px;"><input name='"Data\_block\_1".Pitch' size="10" value=':="Data\_block\_1".Pitch:' type="text"> deg.</p>

</td>

</tr>

<tr style="height: 2%;">

<td colspan="2">

<input type="submit" value="Submit override settings and values">

</td>

</tr>

</form>

<tr style="vertical-align: top; height: 2%;">

<td style="width: 25%;"><p>Braking:</p></td>

<td>

<form method="POST" action="">

<p> <input name='"Data\_block\_1".Braking' size="10" value=':="Data\_block\_1".Braking:' type="text"> %</p>

</form>

</td>

</tr>

<tr><td></td></tr>

</table></body></html>

## Wind\_turbine.css

BODY {

    background-image: url('./Wind\_turbine.jpg');

    background-position: 0% 0%;

    background-repeat: no-repeat;

    background-size: cover;

}

H2 {

    font-family: Arial;

    font-weight: bold;

    font-size: 14.0pt;

    color: #FFFFFF;

    margin-top:0px;

    margin-bottom:10px;

}

P {

    font-family: Arial;

    font-weight: bold;

    color: #FFFFFF;

    font-size: 12.0pt;

    margin-top:0px;

    margin-bottom:0px;

}

TD.Text {

    font-family: Arial;

    font-weight: bold;

    color: #FFFFFF;

    font-size: 12.0pt;

    margin-top:0px;

    margin-bottom:0px;

}

---

#### Configuration in STEP 7 of the example Web page

To include the "Remote Wind Turbine Monitor" HTML page as a user-defined Web page for the S7-1200, you configure the data about the HTML page in STEP 7 and create data blocks from the HTML page.

Access the CPU Properties for the S7-1200 that controls the wind turbine, and enter the configuration information in the User-defined pages properties of the Web Server:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/0w4j2FJdxR4Ip3XvTP1rOA-VBkTPlmjVZAl17lebjV9hA/content?v=9b42bddae620b06d)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/0w4j2FJdxR4Ip3XvTP1rOA-VBkTPlmjVZAl17lebjV9hA)

## Configuration fields

- HTML directory: This field specifies the fully-qualified pathname to the folder where the default page (home page or start page) is located on the computer. The "..." button allows you to browse to the folder that you need.
- Default HTML page: This field specifies the filename of the default page or home page of the HTML application. The "..." button allows you to select the file that you need. For this example, WindTurbine.html is the default HTML page. The Remote Wind Turbine Monitor example only consists of a single page, but in other user-defined applications the default page can call up additional pages from links on the default page. Within the HTML code, the default page must reference other pages relative to the HTML source folder.
- Application name: This optional field contains the name that the Web browser includes in the address field when displaying the page. For this example, it is "Remote Wind Turbine Monitor", but you can use any name.

No other fields require configuration.

## Final steps

To use the Remote Wind Turbine Monitor as configured, generate the blocks, [program the WWW instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/axkwnbW6OmPr8jiifBQdIQ?section=X6877d7f3022562c80e2844ed75aca5d8) with the number of the generated control DB as an input parameter, download the program blocks, and put the CPU in run mode.

When an operator subsequently accesses the standard Web pages for the S7-1200 that controls the wind turbine, the "Remote Wind Turbine Monitor" Web page is accessible from the "User-defined pages" link on the navigation bar. This page now provides the means to monitor and control the wind turbine.

---

### Setting up user-defined Web pages in multiple languages


---

#### Introduction

The Web server provides the means for you to provide user-defined Web pages in the following languages:

- German (de)
- English (en)
- Spanish (es)
- French (fr)
- Italian (it)
- Simplified Chinese (zh)

You do this by setting up your HTML pages in a [folder structure](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/D9h~SOULZpSoCYx0EO_KbQ?section=Xf33dffb2ba1023020bdc9ac9e82394f3) that corresponds to the languages and by [setting a specific cookie named "siemens\_automation\_language" from your pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/LcO~uA8Y2E_rtm51Sjdikg?section=Xfb750477a4014d2925fab292c6729660). The Web server responds to this cookie, and switches to the default page in the corresponding language folder.

---

#### Creating the folder structure

To provide user-defined Web pages in multiple languages, you set up a folder structure under your HTML directory. The two-letter folder names are specific and must be named as shown below:

|  |  |
| --- | --- |
|  | de: German  en: English  es: Spanish  fr: French  it: Italian  zh: Simplified Chinese |

At the same level, you can also include any other folders that your pages need, for example, folders for images or scripts.

You can include any subset of the language folders. You do not have to include all six languages. Within the language folders, you create and program your HTML pages in the appropriate language.

---

#### Programming the language switch

The Web server performs switching between languages through the use of a cookie named "siemens\_automation\_language". This is a cookie defined and set in the HTML pages, and interpreted by the Web server to display a page in the appropriate language from the language folder of the same name. The HTML page must include a JavaScript to set this cookie to one of the pre-defined language identifiers: "de", "en", "es", "fr", "it', or "zh".

For example, if the HTML page sets the cookie to "de", the Web server switches to the "de" folder and displays the page with the default HTML page name as defined in the [STEP 7 configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/lc2uvcOKCUpjfXx3vPnV8Q?section=X879b20b72ec74287b583b3e234b84289).

## Example

The following example uses a default HTML page named "langswitch.html" in each of the language folders. Also in the HTML directory is a folder named "script". The script folder includes a JavaScript file named "lang.js". Each langswitch.html page uses this JavaScript to set the language cookie, "siemens\_automation\_language".

## HTML for "langswitch.html" in "en" folder

The header of the HTML page sets the language to English, sets the character set to UTF-8, and sets the path to the JavaScript file lang.js.

**<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Language" content="en"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Language switching english page</title><script type="text/javascript" src="script/lang.js" ></script>**

The body of the file uses a select list for the user to select between German and English. English ("en") is pre-selected for the language. When the user changes the language, the page calls the DoLocalLanguageChange() JavaScript function with the value of the selected option.

**<!-- Language Selection --><table>**   **<tr>      <td align="right" valign="top" nowrap>       <!-- change language immediately on selection change -->          <select name="Language"                    onchange="DoLocalLanguageChange(this)"                    size="1">            <option value="de" >German</option>            <option value="en" selected >English</option>           </select>      </td>   </tr></table><!-- Language Selection End-->**

## HTML for "langswitch.html" in "de" folder

The header for the German langswitch.html page is the same as English, except the language is set to German.

**<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Language" content="de"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Sprachumschaltung Deutsche Seite</title><script type="text/javascript" src="script/lang.js" ></script></head>**

The HTML in the German page is identical to that of the English page, except that the default value of the selected language is German ("de").

**<!-- Language Selection --><table>   <tr>     <td align="right" valign="top" nowrap>       <!-- change language immediately on change of the selection -->       <select name="Language"               onchange="DoLocalLanguageChange(this)"               <size="1">            <option value="de" selected >Deutsch</option>            <option value="en" >Englisch</option>       </select>      </td>   </tr></table><!-- Language Selection End-->**

## JavaScript "lang.js" in "script" folder

The function "DoLocalLanguageChange()" is in the lang.js file. This function calls the "SetLangCookie()" function and then reloads the window that is displaying the HTML page.

The function "SetLangCookie()" constructs an assignment that assigns the value from the select list to the "siemens\_automation\_language" cookie of the document. It also sets the path to the application so that the switched page, and not the requesting page, receives the value of the cookie.

Optionally, in the commented section, the page could set an expiration value for the cookie.

**function DoLocalLanguageChange(oSelect) {**

**SetLangCookie(oSelect.value);**

**top.window.location.reload();**

**}**

**function SetLangCookie(value) {**

**var strval = "siemens\_automation\_language=";**

**//** **This is the cookie by which the Web server**

**//** **detects the desired language**

**//** **This name is required by the Web server.**

**strval = strval + value;**

**strval = strval + "; path=/ ;";**

**//** **Set path to the application, since otherwise**

**//** **path would be set to the requesting page**

**//** **and this page would not get the cookie.**

**/\* OPTIONAL**

**use expiration if this cookie should live longer**

**than the current browser session:**

**var now = new Date();**

**var endttime = new Date(now.getTime() + expiration);**

**strval = strval + "; expires=" +**

**endttime.toGMTString() + ";";**

**\*/**

**document.cookie = strval;**

**}**

Note:

If your user-defined Web page implementation includes HTML files within language-specific folders (en, de, for example) and also HTML files that are not in the language-specific folders, note that you cannot define enum types with the AWP\_Enum\_Def command in files in both locations. If you use enums, you must define them either within files in the language -specific folders or within files outside of the language-specific folders. You cannot make enum declarations in files in both places.

---

#### Configuring STEP 7 to use a multi-language page structure

The procedure for configuring multi-language user-defined Web pages is similar to the general process for [configuring user-defined Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s7_eTegYUOQrpjL6XHouOA?section=Xe02f10865b52fd8c08edceb8507b84b8). When you have folders set up for languages, however, you set your HTML directory setting to the folder that contains the individual language folders. You do not set the HTML directory to be one of the language folders.

When you select the default HTML page, you navigate into the language folder and select the HTML page that is to be the start page. When you subsequently generate blocks and download the blocks to the CPU, the Web server displays the start page in the language folder that you configured.

|  |  |
| --- | --- |
| For example, if the folder structure shown here was at C:\, the setting for HTML directory would be C:\html, and if English were to be the initial page display, you would navigate to en\langswitch.html for the default HTML page setting. |  |

---

### Advanced user-defined Web page control

When you generate data blocks for your user-defined Web pages, STEP 7 creates a control DB that it uses to control display of and interaction with the user-defined pages. STEP 7 also creates a set of fragment DBs that represent the individual pages. Under normal circumstances, you do not need to know the structure of the control DB or how to manipulate it.

If you want to turn a web application on and off, for example, or manipulate individual manual fragments, you use the control DB tags and the WWW instruction to do so.

## Structure of the control DB

The control DB is an extensive data structure, and is accessible when programming your STEP 7 user program. Only some of the control data block tags are described here.

Note:

Do not make changes in the control DB structure other than changes similar to those described below. Modifications to the control DB structure can prevent the Web server from operating correctly.

## Commandstate structure

"Commandstate" is a structure that contains global commands and global states for the Web server.

The global commands in the "Commandstate" structure apply to the Web server in general. You can deactivate the Web server or restart it from the control DB parameters.

| **Block tag** | **Data type** | **Description** |
| --- | --- | --- |
| init | BOOL | Evaluate the control DB and initialize the Web application |
| deactivate | BOOL | Deactivate the Web application |

**Global states in the Commandstate structure**

The global states apply to the Web server in general and contain status information about the Web application.

| **Block tag** | **Data type** | **Description** |
| --- | --- | --- |
| initializing | BOOL | Web application is reading control DB |
| error | BOOL | Web application could not be initialized |
| deactivating | BOOL | Web application is terminating |
| deactivated | BOOL | Web application is terminated |
| initialized | BOOL | Web application is initialized |
| last\_error | INT | Last error returned from a [WWW instruction call](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/axkwnbW6OmPr8jiifBQdIQ?section=X6877d7f3022562c80e2844ed75aca5d8) when the return code of WWW is 16#0010:  16#0001: fragment DB structure is inconsistent  16#0002: the application name already exists  16#0003: no resources (memory)  16#0004: control DB structure is inconsistent  16#0005: fragment DB not available  16#0006: fragment DB not for AWP  16#0007: enumeration data is inconsistent  16#000D: conflicting size of the control DB |

**Request table**

## Request table

The request table is an array of structures containing commands and states that apply to individual fragment DBs. If you created fragments with the [AWP\_Start\_Fragment](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Iq9OqGiEr7o8kmQC9mTDFQ?section=Xc6b580efab886f310730ca5d372107c9) command of type "manual", the STEP 7 user program must control these pages through the control DB. The request states are read-only and provide information about the current fragment. You use the request commands to control the current fragment.

| **Block tag** | **Data type** | **Description** |
| --- | --- | --- |
| requesttab | ARRAY [ 1 .. 4 ] OF STRUCT | Array of structures for individual fragment DB control.  The Web server can process up to four fragments at a time. The array index for a particular fragment is arbitrary when the Web server is processing multiple fragments or fragments from multiple browser sessions. |

## Struct members of requesttab struct

| **Block tag** | **Data type** | **Description** |
| --- | --- | --- |
| page\_index | UINT | Number of the current web page |
| fragment\_index | UINT | Number of the current fragment - can be set to a different fragment |
| // Request Commands | | |
| continue | BOOL | Enables current page/fragment for sending and continues with the next fragment |
| repeat | BOOL | Enables current page/fragment for resending and continues with the same fragment |
| abort | BOOL | Close http connection without sending |
| finish | BOOL | Send this fragment; page is complete - do not process any additional fragments |
| // Request states | | The request states are read-only |
| idle | BOOL | Nothing to do, but active |
| waiting | BOOL | Fragment is waiting to be enabled |
| sending | BOOL | Fragment is sending |
| aborting | BOOL | User has aborted current request |

## Operation

Whenever your program makes changes to the control DB, it must call the WWW instruction with the number of the modified control DB as its parameter. The global commands and request commands take effect when the STEP 7 user program executes the [WWW instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/axkwnbW6OmPr8jiifBQdIQ?section=X6877d7f3022562c80e2844ed75aca5d8).

The STEP 7 user program can set the fragment\_index explicitly, thus causing the Web server to process the specified fragment with a request command. Otherwise, the Web server processes the current fragment for the current page when the WWW instruction executes.

Possible techniques for using the fragment\_index include:

- Processing the current fragment: Leave fragment\_index unchanged and set the continue command.
- Skip the current fragment: Set fragment\_index to 0 and set the continue command.
- Replace current fragment with a different fragment: Set the fragment\_index to the new fragment ID and set the continue command.

To check global states or request states that might be changing, the STEP 7 user program must call the WWW instruction to evaluate the current values of these states. A typical usage might be to call the WWW instruction periodically until a specific state occurs.

Note:

If the STEP 7 user program sets more than one request command, the WWW instruction processes only one in this order of precedence: abort, finish, repeat, continue. The WWW instruction clears all of the request commands after processing.

## Examples

The following example shows a STEP 7 user program that is checking for a fragment with an ID of 1 to be in the waiting state, following a prior call to the WWW instruction. It might also wait for other application-specific conditions to occur. Then it performs whatever processing is necessary for the fragment, such as setting data block tags, performing calculations, or other application-specific tasks. Afterwards, it sets the continue flag so that the Web server will execute this fragment.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/8JZ5cSNuDd5gEfjcAC8Q~A-VBkTPlmjVZAl17lebjV9hA)

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/FhT64wY~ZVHC6UicwbU~Sw-VBkTPlmjVZAl17lebjV9hA)

When the program calls the WWW instruction with this modified control DB, the user-defined Web page with this fragment can be displayed from the Web browser.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/8JZ5cSNuDd5gEfjcAC8Q~A-VBkTPlmjVZAl17lebjV9hA)

Note that this is a simplified example; the fragment to check could be in any one of the four requesttab structs in the array. Your program must handle all four requesttab structs.

---

### Web API

The S7‑1200 CPU provides a Web API that is an interface for you to read and write process data. The S7‑1200 Web API implements some of the functionality of the S7‑1500 Web API, which is documented below in "Supported Web API methods".

Note that the S7-1200 CPU limits the number of concurrent API sessions to 50.

## Unsupported Web API data types

The S7-1200 Web API supports the S7-1500 Web API supported data types with the exception of the following:

- LWord
- LInt
- ​LTime\_Of\_Day
- ​S5Time
- LDT

You can find the S7‑1500 Web API supported data typesin this [S7-1500 Web server document](https://support.industry.siemens.com/cs/us/en/view/59193560) at the following location: Application Programming Interface (API) > Read and write process data > Supported data types.

## Supported Web API methods

The S7-1200 supports the following Web API methods:

- Api.Ping
- Api.Version
- Api.GetCertificateUrl
- Api.ChangePassword
- Api.GetPasswordPolicy
- Api.GetAuthenticationMode
- Api.Browse
- Api.Login
- Api.Logout
- Api.GetPermissions
- PlcProgram.Browse
- PlcProgram.Write
- PlcProgram.Read
- Syslog.Browse

---

## Constraints


---

### Constraints

The following IT considerations can affect your use of the Web server:

- Typically, you must use the IP address of the CPU to access the standard Web pages or user-defined Web pages, or the IP address of a wireless router with a port number. If your Web browser does not allow connecting directly to an IP address, see your IT administrator. If your local policies support DNS, you can connect to the IP address through a DNS entry to that address.
- Firewalls, proxy settings, and other site-specific restrictions can also restrict access to the CPU. See your IT administrator to resolve these issues.
- The standard Web pages use JavaScript and cookies. If your Web browser settings disable JavaScript or cookies, enable them. If you cannot enable them, some [features are restricted](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/wrP29WrwkfDfqclCKRS3yA?section=X4edb66e08f73aa203082d5bd2067df78). Use of JavaScript and cookies in user-defined Web pages is optional. If used, you must enable them in your browser.
- The Web server supports Transport Layer Security (TLS). You can access the standard Web pages and user-defined Web pages with an URL of either http://ww.xx.yy.zz or https://ww.xx.yy.zz, where "ww.xx.yy.zz" represents the IP address of the CPU.
- Siemens provides a security certificate for secure access to the Web server. From the [Introduction standard Web page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Xg9__n2VjA94jp2nIObq_Q?section=Xd23ae64928a47523b2f84d97f3b38829), you can download and [import the certificate into the Internet options of your Web browser](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/MLhOdcBjbS9SxLjBtqsreA?section=X44c4d41f5bfe40d423bb36671a63bfa0). If you choose to not import the certificate, you will get a security verification prompt every time you access the Web server with https://.

## Number of connections

The Web server supports a maximum of 30 active connections. Various actions consume the 30 connections, depending on the Web browser that you use and the number of different objects per page (.css files, images, JavaScript files, additional .html files). Some connections persist while the Web server is displaying a page; other connections do not persist after the initial connection.

If, for example, you are using certain versions of Mozilla Firefox, which support a maximum of six persistent connections, you could use five browser or browser tab instances before the Web server starts dropping connections. In the case where a page is not using all six connections, you could have additional browser or browser tab instances.

Also be aware that the number of active connections can affect page performance. For this reason, the Web pages may not load fully.

Note:

**Log off prior to closing Web server**

If you have logged in to the Web server, be sure to log off prior to closing your Web browser. The Web server supports a maximum of seven concurrent logins.

Failure to log off can leave multiple connections open, depending on your browser. By opening and closing Web server browser windows multiple times without logging off, you could consume all of the 30 connections. If you consume all of the connections, you would then receive an "Invalid login" message when you attempt to log in. You would have to wait up to 30 minutes before the Web server frees up enough connections for you to log in again. To avoid this problem, always log off before closing the Web server if you have logged in.

---

### Use of JavaScript

The standard Web pages use HTML, JavaScript, and cookies. If your site restricts the use of JavaScript and cookies, then enable them for the pages to function properly. If you cannot enable JavaScript for your Web browser, the standard Web pages cannot run. Consider using the basic pages, which do not use JavaScript.

## See also

[Layout of the standard Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U3H9V2C8QZdfMLd1U4iAtg?section=X44549da8d9a3c84cff32085b67bd151d)

---

### Feature restrictions when the Internet options do not allow cookies

If you disable cookies in your Web browser, the following restrictions apply:

- You cannot log in.
- You cannot change the language setting.
- You cannot switch from UTC time to PLC time. Without cookies, all times are in UTC time.

---

### Rules for entering tag names and values

Be aware of the following conventions when using the [Tag status](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f7WatsxclQNha2u2VG9y0g?section=X37eac0b13e3c4cc90b9bdcbd15642672) and [Watch tables](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/slqDdcEVd6jLXnTqF9vRPg?section=Xc90b523b21099b5ef9875b12ea0cf151) standard pages:

- If modifying the entire value of a DTL tag, for example, "Data\_block\_1\_.DTL\_tag, use the following DTL syntax for the modify value: DTL#YYYY-MM-DD-HH-MM-SS[.sssssssss]
- When using exponential notation to enter a value for a Real or LReal data type:

  - To enter a real-number value (Real or LReal) with a positive exponent (such as +3.402823e+25), enter the value in either of the following formats:

    +3.402823e25

    +3.402823e+25
  - To enter real-number value (Real or LReal) with a negative exponent (such as +3.402823e-25), enter the value as follows:

    +3.402823e-25
  - Be sure that the mantissa portion of the real value in exponential notation includes a decimal point. Failure to include a decimal point results in the modification of the value to an unexpected integer value. For example, enter -1.0e8 rather than -1e8.
- LReal values can be only 15 digits (regardless of the location of the decimal point). Entering more than 15 digits creates a rounding error.

Limitations on the Tag status and Watch Table page:

- The maximum number of characters for the URL is 2083. You can see the URL that represents your current page in the address bar of your browser.
- For the character display format, if the actual CPU values are not valid ASCII characters as interpreted by the browser then the page displays the character preceded by a dollar sign: $.

---

### Importing CSV format data logs to non-USA/UK versions of Microsoft Excel

Data log files are in the comma-separated values (CSV) file format. You can open these files directly in Excel from the Data Logs page when your system is running the USA or UK version of Excel. In other countries, however, this format is not widely used because commas occur frequently in numerical notation.

To open a data log file that you have saved, follow these steps for non USA/UK versions of Excel:

1. Open Excel and create an empty workbook.
2. From the "Data > Import External Data" menu, select the "Import Data" command.
3. Navigate to and select the data log file you want to open. The Text Import Wizard starts.
4. From the Text Import Wizard, change the default option for "Original data type" from "Fixed width" to "Delimited".
5. Click the Next button.
6. From the Step 2 dialog, select the "Comma" check box to change the delimiter type from "Tab" to "Comma".
7. Click the Next button.
8. From the Step 3 dialog, you can optionally change the Date format from MDY (month/day/year) to another format.
9. Complete the remaining steps of the Text Import Wizard to import the file.