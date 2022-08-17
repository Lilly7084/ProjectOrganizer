# ProjectOrganizer v0.1.2

A custom project organizer with dependency checking.

This project was started by a friend (@GenericNerdyUsername), but I decided to take it from
their list (since they already had plenty of unfinished projects). The
`projects.json` file, which currently contains an example project tree, has been
preserved from their version, but the source code has been rebuilt from scratch.

## To-do list

v0.1.0 (Initial test):
- [x] Import a graph from a JSON file
- [x] Positioner type: Random object placement
- [x] Draw a graph to a PyGame window

v0.2.0 (Functionality):
- [x] Positioner type: Dependency tiers
- [ ] Show text contents of nodes
- [ ] Resize nodes to perfectly fit text
- [ ] Scroll preview window for larger graphs
- [ ] Check projects for unsatisfied dependencies
- [x] Export graph to PNG image

v0.3.0 (Aesthetic):
- [ ] Controllable node shape and text wrapping
- [ ] Multiple node forms (ellipse, rectangle, ...)
- [ ] Parse color information from JSON file
- [ ] Show color code in rendered graphs
- [ ] Use cubic curves (Hermite spline?) for dependency lines
- [ ] Add arrow heads to the ends of lines

v0.4.0 (Legibility):
- [ ] Positioner type: Reduce crossing lines
- [ ] Positioner type: Reduce connection lengths
- [ ] Export graph to SVG image
- [ ] Place connections evenly spaced on node's edges
- [ ] Alternate line routing: Clearance/avoidance

v0.5.0 (Usability):
- [ ] Add a command line interface
- [ ] Add a graphical interface to the preview window
- [ ] Add strings file to prepare for translation
- [ ] Create icon files (vector image and 128x128)
- [ ] Release as a portable executable

## Project-list format

_Coming soon! For now, use the `projects.json` file as a reference._

## Color code

_Not actually working yet! Will be added for v0.3.0._

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

[1] This tag is never assigned to an item. Rather, it's automatically assigned
    to any project with at least one unsatisfied (incomplete) dependency.

## How to run

It's quite simple, just run `python main.py <path>`, providing a path to a
JSON file describing your current project list.
