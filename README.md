# collect_with_ansible

It is an example ansible project to use custom logger for store the log entries on the ansible server.
There are two components in this setup:
 - custom module to collect information on the ansible host
 - custom callback plugin that filter our custom log entries and save to a log folder.

# Use case

You have some hundred servers and need a real-time inventory about their states.
- Edit your ansible hosts file
- Define the collector in the library folder (how many postgresql running, whos is master and who is backup, how much free space you have, which java is installed, what is the java memory setup, ...)
- Define the logging method in the custom_logger (use separate files for each host or log into a mongo database)
- Run your playbook

    ansible-playbook --inventory=hosts my_collector.yml
