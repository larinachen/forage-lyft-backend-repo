# Software Architecture

## Design Needs:
* easy to change which mechanical parts the car model includes & represent new car models
* trivial work needed to add new service criteria: update to criteria should only needs to be implemented one time

## Classes:
* engine (super class): current mileage, last service mileage, warning light state (on/off)
     * capulet engine subclass, sternman subengine class, willoughby engine subclass (inherited from super class)
     * __init__, engine_should_be_serviced

* battery (super class): current date, last service date
    * spindler battery subclass, nubbin battery subclass (inherited from super class)

* model (base class): engine, battery
    * __init__, needs_service (if either battery or engine needs service)