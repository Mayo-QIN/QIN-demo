# Mayo Radiology Informatics Lab Demo

Workflow is an important component of the [Quantative Imaging Network(QIN)](https://imaging.cancer.gov/informatics/qin.htm).  For the face-to-face meeting in April 2017, this demonstration project will show the utility of [`grunt`](https://github.com/Mayo-QIN/grunt) and [TACTIC](https://github.com/Southpaw-TACTIC/TACTIC) to store, process and orchestrate workflow.  Using Docker and Docker Compose, a "cluster" of machines is created containing a DICOM ingestion system, TACTIC, [Consul](https://www.consul.io/), and several grunt-enabled processing algorithms.

## Start up

```bash
docker-compose up
```

## Tutorial

To execute the tutorial follow the steps:


Start up the infrastructure described in the yml file of docker compose. The services that have been implemented in this demo are:


- Tactic (CMS)(port: 9907)
- Dicom receiver (dcmtk)(port: 9902)
- Slicer (port: 9904)
- riipl (port: 9901)
- dcmqi (port: 9905)
- Python machine learning (port: 9908)

### send data.


We choose to use dcm4che (DCMTK although it was used as a receiver could not handle the DCO object)

```
./dcmsnd receiver@localhost:9902 {folder or file}
```



# Acknowledgement
Supported by the NCI Grant CA160045
