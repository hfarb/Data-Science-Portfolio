* Data Engineering Portfolio

** 3 Projects:

1. Big Analytics Using Google BigQuery: In this project, I practiced with SQL while learning about the Google Cloud Platform (GCP) and BiqQuery. I answered two business-driven questions using public datasets housed in GCP. I used the datasets in different ways through the web UI (BiqQuery) and command-line tools and worked with them in Jupyter Notebook.

In the project, I acted as a data scientist at Lyft Bay Wheels, tryinng to increase ridership through offering deals in mobile app. I used data from the static tables in the dataset san_francisco on Google BitQuery:

    * bikeshare_stations

    * bikeshare_status

    * bikeshare_trips
    
and used SQL to answer two questions:
    1. What are the 5 most popular trips that I would call "commuter trips"?
    2. What are my recommendations for offers (justify based on your findings)?

Findings: The five most popular commuter trips are
    1. San Francisco Caltrain 2 (330 Townsend) to Townsend at 7th
    2. Harry Bridges Plaza (Ferry Building) to 2nd at Townsend
    3. 2nd at Townsend to Harry Bridges Plaza (Ferry Building)
    4. Embarcadero at Sansome to Steuart at Market
    5. San Francisco Caltrain (Townsend at 4th) to Harry Bridges Plaza (Ferry Building).

Because most bike trips are made by subscribers and most subscribers appear to be commuters that ride bikes for less than 30 minutes, I suggest either increasing the amount of the monthly or yearly membership fee or decreasing the amount of time per trip that is included as a part of the membership with no additional fee. I also suggest increasing marketing and awareness for the corporate memberships deal since most of the subsribers appear to be commuters to and from and work.

2. In this project, I take on the roll of an ed tech firm employee. I've hypothetically created a service that
delivers assessments, and now lots of different customers (e.g., Pearson) want
to publish their assessments on it. The goal of this project is to get ready for data scientists
who work for these customers to run queries on the data. In this project,I: 
    - Publish and consume messages with Kafka
    - Use Spark to transform the messages. 
    - Use Spark to transform the messages so that you can land them in HDFS

3. In this project, I take on the roll of a data scientist at a game developmennt company. The company's latest mobile game has two events I'm interested in tracking: `buy a sword` & `join guild` and each has metadata characterstic of such events (i.e., sword type, guild name,etc). In this project, I:

- Instrument my API server to log events to Kafka

- Assemble a data pipeline to catch these events: use Spark streaming to filter
  select event types from Kafka, land them into HDFS/parquet to make them
  available for analysis using Presto

- Use Apache Bench to generate test data for my pipeline

- Produce an analytics report where I provide a description of my pipeline
  and some basic analysis of the events

Note: It's understood that events in this pipeline are _generated_ events which make
them hard to connect to _actual_ business decisions.  However, it's an opportunnity for me to demonstrate an ability to plumb this pipeline end-to-end, which includes initially generating test data as well as submitting a notebook-based
report of at least simple event analytics.

