# Productivity

## DB Code Management System
    ongoing

## Fully deployed dev environment
    WIP

## Isolated or parallel feature/version development 
    eg 2 teams working on 4.10 and 2 teams working on 4.11



# Quality

## Enhancement of Continuous Integration process
    why: faster feedback to developers. 
    how: multi-level testing: 
        component (unit) tests & component integration tests in 10 mins -> per code revision
        system integration tests in 2hrs includes infrastructure -> per build
        system tests in 8h -> nighlty build


## Integration tests
    1. dedicated test apps
    2. testing by means of RPC

## Performance tests
    1. load/stress testing 
    2. scalability
    3. HW sizing

# Design

## Scalable solutions
    why: break down the current monolithic architecture and deployment. allow the use of multiple machines (vms) to run the semperdata system. better performance in virtualized environments, more flexible deployments according to customer needs. 
    how: multi-instance app servers. Define performance requirements of those and test them. 

## Bring new technologies into product
    why: there are dedicated solutions for given functionalities. it's much faster, scalable and reliable to use them instead of building our own or working around the lack of technical support.
    how: MongoDB (DA), Redis (queues, distributed locks), etcd (distributed configuration manager), SignalR (bi-directional distributed messaging - eg. UI-app communication)

## Easily Generate new products from existing code base
    1. code separation 
    2. re-engineer deployment process, install kits and update packages.

# Security (applications)

## Upgrade Dicom toolkit
    why: uses an old OpenSSL version, unsuported and not up-to-date


