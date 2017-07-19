# collect_with_ansible

It is an example ansible project to use custom logger for store the log entries on the ansible server.
There are two components in this setup:
 - custom module to collect information on the ansible host
 - custom callback plugin that filter our custom log entries and save to a log folder.
