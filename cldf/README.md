<a name="ds-genericmetadatajson"> </a>

# Generic Phlorest phylogeny derived from Zhang et al 2019 'Sino-Tibetan (Zhang et al. 2019)'

**CLDF Metadata**: [Generic-metadata.json](./Generic-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Zhang M, Yan S, Pan W, & Jin L. 2019. Phylogenetic evidence for Sino-Tibetan origin in northern China in the Late Neolithic. Nature, 569, 112–115.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://doi.org/10.1038/s41586-019-1153-z
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/2.0/
[dc:subject](http://purl.org/dc/terms/subject) | <dl><dt>family</dt><dd>Sino-Tibetan</dd><dt>analysis</dt><dd>bayesian</dd><dt>scaling</dt><dd>years</dd></dl>
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/phlorest/zhang_et_al2019
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="data.nex">data.nex </a></li><li><a href="https://github.com/phlorest/zhang_et_al2019/tree/3a79ceb">phlorest/zhang_et_al2019 3a79ceb</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.8">Glottolog v4.8</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.10.6</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | zhang_et_al2019
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

The LanguageTable lists the taxa, i.e. the leafs of the phylogeny, mapped to languoids.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 109


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
`isocode` | `string` | 
`Glottolog_Name` | `string` | 

## <a name="table-treescsv"></a>Table [trees.csv](./trees.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF TreeTable](http://cldf.clld.org/v1.0/terms.rdf#TreeTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1001


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | Name of tree as used in the tree file, i.e. the tree label in a Nexus file or the 1-based index of the tree in a newick file
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | Describe the method that was used to create the tree, etc.
[Tree_Is_Rooted](http://cldf.clld.org/v1.0/terms.rdf#treeIsRooted) | `boolean` | Whether the tree is rooted (Yes) or unrooted (No) (or no info is available (null))
[Tree_Type](http://cldf.clld.org/v1.0/terms.rdf#treeType) | `string` | Whether the tree is a summary (or consensus) tree, i.e. can be analysed in isolation, or whether it is a sample, resulting from a method that creates multiple trees
[Tree_Branch_Length_Unit](http://cldf.clld.org/v1.0/terms.rdf#treeBranchLengthUnit) | `string` | The unit used to measure evolutionary time in phylogenetic trees.
[Media_ID](http://cldf.clld.org/v1.0/terms.rdf#mediaReference) | `string` | References a file containing a Newick representation of the tree, labeled with identifiers as described in the LanguageTable (the [Media_Type](https://cldf.clld.org/v1.0/terms.html#mediaType) column of this table should provide enough information to chose the appropriate tool to read the newick)<br>References [media.csv::ID](#table-mediacsv)
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)

## <a name="table-mediacsv"></a>Table [media.csv](./media.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) | `string` | 
[Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl) | `anyURI` | 
[Path_In_Zip](http://cldf.clld.org/v1.0/terms.rdf#pathInZip) | `string` | 

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

The ParameterTable lists characters (a.k.a. sites), i.e. the (often binary) variables used as data basis to compute the phylogeny from.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 949


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Sequence index of the site in the corresponding Nexus file.<br>Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[ColumnSpec](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) | `json` | 
[Nexus_File](http://cldf.clld.org/v1.0/terms.rdf#mediaReference) | `string` | The data for this parameter is stored at 1-based index {ID} of the sequences in the DATA block of the Nexus file specified here. (See https://en.wikipedia.org/wiki/Nexus_file)<br>References [media.csv::ID](#table-mediacsv)

