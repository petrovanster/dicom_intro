## Dicom standard
what is it?
how is it maintained?


## Dicom informational models
modules
tags
sample tags
identifiers - 

## Communication

## Commands
C-s
N-s

# DIMSE

## SOP
A Service-Object Pair (SOP) Class is defined by the union of an Information Object Definition (IOD) and a DICOM Service Elements (DIMSE). The SOP Class definition contains the rules and semantics which may restrict the use of the services in the DIMSE Service Group or the Attributes of the IOD.

Examples of Service Elements are Store, Get, Find, Move, etc.
Examples of Objects are CT images, MR images, but also include schedule lists, print queues, etc.

https://www.dicomlibrary.com/dicom/sop/

## Abstract syntax
 The Abstract Syntax identifies one SOP Class or a Meta SOP Class. The presentation context consists of the Abstract Syntax (what information is exchanged) and the Transfer Syntax (how it is encoded) used for that abstract syntax.

## Transfer syntax
A Transfer Syntax is a set of encoding rules able to unambiguously represent one or more Abstract Syntaxes. In particular, it allows communicating Application Entities to negotiate common encoding techniques they both support (e.g., byte ordering, compression, etc.).
A Transfer Syntax is an attribute of a Presentation Context, one or more of which are negotiated at the establishment of an Association between DICOM Application Entities.

eg. https://www.dicomlibrary.com/dicom/transfer-syntax/

## Dicom conformance 

eg: https://www.softneta.com/documentation/dicom-conformance-statement/supported-sop-classes/ 

## Presentation Contexts
sample negotiation

## Imaging specific tags
transfer syntax - compression

