This repo uses a google spreadsheet to power [hugo](http://gohugo.io). 

The result is an HTML website with detail pages for abstracts, an 
index of PIs, and a list of abstracts, broken down by PI. 

Example site here: https://seandavi.github.io/genetics_branch_retreat_site/

## Prereqs

- hugo needs to be installed (`brew install hugo`)
- Assumes that a google doc with specific columns is available and 
has been filled using something like google forms
- each row is an abstract
- Google spreadsheet has been *published as a csv download link*

## Modification for new material (new year, for example)

- Change information in `config.toml` to match new meeting
- Change URL in `make_abstracts.sh`
- Adjust columns in `archetypes/abstract.md` (as needed)
- Run `make_abstracts.sh`

## Preview site

- `hugo serve`

## Build site

- `hugo`
- [optional] `ghp-import -p -f public` (assumes that you are importing to a github pages site, but any web hosting system will work). 


