# ProjectOrganizer v0.2.1

A visual project organizer with dependency checking.

**UPDATE**: Since the approach we were trying in 2022 wasn't working (too much
graph theory, etc.), we ripped up the entire code base and replaced it with an
almost absurdly simple, single-file solution built around the
[D2 diagram scripting language](https://github.com/terrastruct/d2).

This project was started by a friend (@GenericNerdyUsername), but I decided to
take it from their list (since they already had plenty of unfinished projects).
The `projects.json` file, which currently contains an example project tree, has
been preserved from their version, but the source code has been rebuilt from
scratch.

It is licensed under GPLv3.

Here's an example of what it's outputting right now:

![test graph output](./test.svg)

## Project-list format

_Coming soon! For now, use the `projects.json` file as a reference._

## Color code

To make it more clear what can and can't be done at any given time, projects are
usually color-coded. The color code can be defined on a per-project basis, and
can be whatever you want, but will default to:

| Tag             | Color  | Description                                      |
|-----------------|--------|--------------------------------------------------|
| stalled         | Orange | Delayed due to complications or lack of interest |
| failed          | Red    | Cancelled/abandoned due to complications/failure |
| abandoned       | Red    | Cancelled/abandoned due to lack of interest      |
| in progress     | Blue   | Currently being worked on                        |
| completed       | Green  | Finished and functional, but may be revisited    |
| available       | Black  | Not yet started                                  |
| missing deps[1] | Gray   | Can't start due to missing dependencies          |
| default         | Black  | (No specific meaning)                            |

[1] This tag doesn't need to be assigned manually; the script will automatically
    check every dependency of a project, and assign the tag as necessary. It can
    still be set on its own, to mark dependency-related issues which aren't the
    result of other projects not being completed.

## How to run

It's quite simple, just run `/path/to/proj_org.py <path>`, providing a path to a
JSON file describing your current project list. If the script has been marked as
executable (`chmod +x`), you don't even need to add a `python3` at the start.
