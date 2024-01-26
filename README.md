- [Some pre-requisites](#org318e3eb)
  - [Installing micromamba](#org56e756d)
  - [Configuring the environment](#org34c3420)
- [Get Appraise ready](#org425d42e)
- [Get the example ready](#org822698f)
  - [Generating the manifest.json](#orgd849e6b)
  - [Generating the batches.json](#org4310010)
    - [The task description](#org57f66c6)
    - [The item description](#org8b83454)
  - [Creating the campaign](#org4ce220c)
- [Testing the campaign](#org9bed4a3)



<a id="org318e3eb"></a>

# Some pre-requisites


<a id="org56e756d"></a>

## Installing micromamba

Micromamba is a environment & package manager tool relying on the conda ecosystem. It is useful to ensure the reproducibility of the environment (i.e., that everyone plays with same version of the packages) The installation is pretty straightfoward and relies on the following command:

```sh
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

It is strongly recommended to use the defaults values (so just press enter everytime). You have to restart your shell for everything to be activated.


<a id="org34c3420"></a>

## Configuring the environment

Now that micromamba is installed, you can create the conda environment dedicated to Appraise. To do so, simply open a terminal and go to the directory containing this README. Then, run the following command:

```sh
conda env create -f attachments/appraise_environment.yaml
```

Finally, you activate the environment using the following command

```sh
conda activate appraise
```

The environment creation should be only done once. However, the activation should be done everytime you open a terminal and want to use this environment (logical, isn't it? :D)<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>.


<a id="org425d42e"></a>

# Get Appraise ready

Now that we have our environment ready, it is time to configure Appraise. To do so, the first step consists of cloning the repository and then going to the directory:

```sh
git clone https://github.com/AppraiseDev/Appraise.git
cd Appraise
```

Next, we need to boostrap the database. This is done in 2 substeps. First, we need to migrate some data:

```sh
python manage.py migrate
```

Then, we have to create a superuser (the admin user):

```sh
python manage.py createsuperuser
```

Fill the information (username, email, password) as you need (I suggest to keep it easy **during the prototyping phase** - same username/password despite the complain of the script.)

The last part aims to collect the static information required to start a dashboard. This is done as follows:

```sh
python manage.py collectstatic --no-post-process
```

At this stage, Appraise is ready to host evaluation campaigns. We now have to create one :D.


<a id="org822698f"></a>

# Get the example ready

The example we are going to play with is stored in <attachments/DataTest/>. I suggest to copy this directory to the subdirectory `Examples` of Appraise.


<a id="orgd849e6b"></a>

## Generating the manifest.json

For the manifest it is easier to create it manually for now. The content should be as follow:

```json
{
  "CAMPAIGN_URL": "http://127.0.0.1:8000/dashboard/sso/",
  "CAMPAIGN_NAME": "exampleDataSet",
  "CAMPAIGN_KEY": "c10",
  "CAMPAIGN_NO": 10,
  "REDUNDANCY": 1,
  "TASKS_TO_ANNOTATORS": [
    [
      "eng",
      "spa",
      "uniform",
      1,
      1
    ]
  ],
  "TASK_TYPE": "Data"
}
```

The fields are the following:

-   **`CAMPAIGN_URL`:** the base URL of the campaign
-   **`CAMPAIGN_NAME`:** the name of the campaign (**it should not contains underscores!!**)
-   **`CAMPAIGN_KEY`:** an identifier of the campaign
-   **`CAMPAIGN_NO`:** the number of the campaign (useful when want to run )
-   **`REDUNDANCY`:** ???
-   **`TASKS_TO_ANNOTATORS`:** contains 4 information:
    1.  the source language (here "eng" for english, **the code are defined in the tool and should be respected**)
    2.  the target language (here "spa" for spanish)
    3.  ???
    4.  ???
-   **`TASK_TYPE`:** The type of evaluation campaign. In our case, we selected the simples (Data) and the strategy is implemented in [Appraise/EvalData/models/data<sub>assessment.py</sub>](https://github.com/appraiseDev/Appraise/blob/main/EvalData/models/data_assessment.py) (note that Data &rArr; `data(_assessment`!!)


<a id="org4310010"></a>

## Generating the batches.json

To generate the batches.json, we need to think about 2 key informations:

1.  the task description
2.  the item description

Assuming the files [en.json](attachments/DataTest/en.json) and [sp.json](attachments/DataTest/sp.json), call the script [generate<sub>batch.py</sub>](attachments/DataTest/generate_batch.py) will generate the files batches.json. To call this script, it is pretty easy, just do this in the proper directory:

```sh
python generate_batch.py
```


<a id="org57f66c6"></a>

### The task description

The task description is described by this block:

```json
"task": {
  "batchNo": 1,
  "batchSize": 100,
  "randomSeed": 1111,
  "requiredAnnotations": 1,
  "sourceLanguage": "eng",
  "targetLanguage": "spa"
}
```

Some information about the different fields:

-   **batchNo:** the number of the batch
-   **batchSize:** has to be 100
-   **randomSeed:** a random seed
-   **requiredAnnotations:** the number of annotations required per items
-   **sourceLanguage:** the language of the source document (here English, again be careful with the code)
-   **targetLanguage:** the language of the target document (here Spanish)


<a id="org8b83454"></a>

### The item description

While for each block, there is only one task, there are multiple items. As a result, the field "items" is a list in the json file. One item corresponds to one document in both the source and the target languages. Each item is described as follows:

```json
{
  "_block": -1,
  "_item": 0,
  "documentDomain": "Unknown",
  "itemID": 1,
  "itemType": "TGT",
  "sourceID": "eng.1",
  "sourceText": "We bought one for road trips and trying to interpret maps without having to strain our eyes.\nReally nice design, good tactile feel.\nI couldn't figure out where the batteries were, sent Lightwedge Customer Service an email and received a response within 24 hours.\nIf you need one I'd recommend this one.",
  "sourceURL": "Unknown",
  "targetID": "spa.1",
  "targetText": "Compramos uno para los viajes por carretera y para poder interpretar mapas sin tener que forzar la vista.\nRealmente tiene un dise\u00f1o bonito y una buena sensaci\u00f3n t\u00e1ctil.\nNo pod\u00eda encontrar d\u00f3nde estaban las pilas, envi\u00e9 un correo electr\u00f3nico al servicio de atenci\u00f3n al cliente de Lightwedge y recib\u00ed una respuesta en menos de 24 horas.\nSi necesitas uno, te recomendar\u00eda este.",
  "targetURL": "Unknown"
},
```

Again, here are the fields:

-   **\_block:** should be -1
-   **\_item:** the index of the item (starting 0)
-   **documentDomain:** the domain of the document (user defined but generally corresponds to the pool of the document)
-   **itemID:** \_item + 1 &rArr; the rank of the item
-   **itemType:** it could take values in TGT (Target), SRC (Source), REF (Reference), BAD (Bad Reference), CHK (Redundancy checking)
-   **sourceID:** the identifier of the source document
-   **sourceText:** the content of the source document. Each sentence is separated by the non-special sequence '\n'
-   **sourceURL:** the URL of the source document
-   **targetID:** the identifier of the target document
-   **targetText:** the content of the target document. Each sentence is separated by the non-special sequence '\n'
-   **targetURL:** the URL of the target document


<a id="org4ce220c"></a>

## Creating the campaign

After creating the needed files, we are now ready to create the campaign. To do so, run the following command:

```sh
export EX_DIR=Examples/DataTest; python manage.py StartNewCampaign $EX_DIR/manifest.json --batches-json $EX_DIR/batches.json --csv-output $EX_DIR/output.csv
```

While this command looks intimidating, it is actually a pretty straightforward one when you decompose it:

-   **`export EX_DIR=Examples/DataTest`:** is creating a bash variable to avoid having to enter several time the directory. In our case, we use it to point to the directory of our example
-   **`$EX_DIR/manifest.json`:** points to the manifest.json file created earlier
-   **`--batches-json $EX_DIR/batches.json`:** points to the batch.json file created earlier
-   **`--csv-output $EX_DIR/output.csv`:** indicate where generate the metadata related to the campaign. This will be necessary in the next section


<a id="org9bed4a3"></a>

# Testing the campaign

First thing is to start the HTTP server:

```sh
python manage.py runserver
```

It should show something like this:

```
System check identified no issues (0 silenced).
August 09, 2023 - 15:53:42
Django version 3.2.19, using settings 'Appraise.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The important information in this part is "<http://127.0.0.1:8000/>" showing the server in only accessible from the localhost (your machine!) and the port 8000.

To test the campaign, the next step is to simply go to the URL of the campaign. To do so, simply open the file "Examples/DataTest/output.csv" which should look like this:

```csv
Username,Password,URL
engspa0a01,d02ee011,http://127.0.0.1:8000/dashboard/sso/engspa0a01/d02ee011/
```

The information will be different on your side, but the format should be identical. To test the campaign, go to the URL indicated as the 3rd field of the CSV file and follow the instructions from there.

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> For more information about conda, I suggest to use this useful reference card: <https://images.datacamp.com/image/upload/v1681474450/Marketing/Blog/Conda_Cheat_Sheet_1.pdf>. When using micromamba, replace each call of "conda" by "micromamba" or create an alias :D