# Mayo Radiology Informatics Lab Demo

Workflow is an important component of the [Quantative Imaging Network(QIN)](https://imaging.cancer.gov/informatics/qin.htm).  For the face-to-face meeting in April 2017, this demonstration project will show the utility of [`grunt`](https://github.com/Mayo-QIN/grunt) and [TACTIC](https://github.com/Southpaw-TACTIC/TACTIC) to store, process and orchestrate workflow.  Using Docker and Docker Compose, a "cluster" of machines is created containing a DICOM ingestion system, TACTIC, [Consul](https://www.consul.io/), and several grunt-enabled processing algorithms.

## Start up

```bash
docker-compose up
```

## Tutorial

