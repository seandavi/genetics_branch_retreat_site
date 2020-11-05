This repo uses a google spreadsheet to power [hugo](http://gohugo.io). 

The result is an HTML website with detail pages for abstracts, an 
index of PIs, and a list of abstracts, broken down by PI.

# Prereqs

- Assumes that a google doc with specific columns is available and 
has been filled using something like google forms
- each row is an abstract
- Google spreadsheet has been published as a csv download link

# Modification for new material (new year, for example)

- Change information in `config.toml` to match new meeting
- Change URL in `make_abstracts.sh`
- Adjust columns in `archetypes/abstract.md`
- Run `make_abstracts.sh`

# Preview site

- `hugo serve`

# Build site

- `hugo`
- `ghp-import -p -f public`


