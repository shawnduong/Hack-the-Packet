# Hack the Packet

"Hack the Packet!" was an event that occurred at UC Merced on 2022-11-07, hosted by Shawn Duong, Isabella Montoya, and Porfirio Montoya of HackMerced and UC Merced ACM SIG Cybersecurity.

Organizers connected to the network switch to inject network traffic; 5 million packets captured on real open networks were replayed in addition to artificially injected logins. Participants of this event connected to a network switch and were challenged to find logins. Teams were rewarded for finding logins, whether real or artificial, and these were displayed on a projector at the front of the room.

This event was heavily inspired by the [Wall of Sheep](https://www.wallofsheep.com/pages/wall-of-sheep).

## General Setup

Replace `wordlists/websites.txt` with a wordlist of websites and `wordlists/usernames.txt` with a list of usernames.

## Replay Setup

As an organizer, connect to the network switch and run `./main.py <iface> <cap>`, where `<iface>` is the interface corresponding to the connection with the network switch and `<cap>` is a packet capture file collected from a real network.

Participants should begin seeing traffic if they're connected to the network switch.

## Website Setup

Run `webpage/main.py` and a website will be started at http://127.0.0.1:8080. In order to initialize the teams, run `webpage/scripts/initialize_teams.sh`. This will make teams Alpha to Echo.

To add an entry to the website, run `webpage/scripts/add_entry.sh`. Syntax:

```sh
./add_entry.sh <team name> <user> <pass> <site>
```

## Acknowledgements

`wordlists/passwords.txt` is the first 10000 lines of rockyou.txt. `wordlists/directories.txt` is the `directory-list-2.3-small.txt` from dirbuster (credits to James Fisher).
