# Nutcracker

A Python program for converting NutMan (`.nm2`) files to a JSON format.

## Why?

The NutMan file format is simple: it's just a text file with headers (denoted by `###` lines) and key-value pairs. While this is slow, it's also very easy to convert to other more standard formats like JSON. This particular conversion makes the data more compact and much more portable.

## End Goal

Once you've converted your `.nm2` file to JSON, it can be read easily by other programs. This allows you to view and edit your data outside of NutMan's archaic and confining interface.

Right now, Nutcracker can only convert your files. It doesn't have any editing capabilities yet. That's in the works though... stay tuned!

