# comfyui_otonx_nodes

Repository: Otonx's Custom Nodes for ComfyUI.

**Note:** Nodes in this repository are subject to intermittent changes. Please review and test nodes thoroughly prior to integration.

---

### OTX KSampler Feeder

**Description:** Centralized value storage for input parameters intended for the KSampler (Advanced) nodes. Designed based on the workflow outlined in [Advanced SDXL Workflows in ComfyUI](https://followfoxai.substack.com/p/part-4-advanced-sdxl-workflows-in).

**Outputs:**
- **seed_number:** Interface for both Base KSampler and Refiner KSampler nodes.
- **steps:** Maintains a consistent 'steps' value between the base and refiner samplers.
- **cfg:** Allows identical cfg values to be set for both base and refiner samplers.
- **base_steps_portion:** Outputs a value that can synchronize the `start_at_step` of the refiner with the `end_at_step` of the base.

**Utility:** Reduces the need for multiple primitive nodes containing singular values, centralizing configuration.

---

### OTX Versatile Multiple Inputs

**Description:** A multi-input node allowing for the definition of up to five values, each accompanied by its data type specification (INT, FLOAT, or STRING).

**Functionality:** Users can define the data value and type for each of the five slots, ensuring accurate data type handling for downstream nodes.

**Utility:** Provides a flexible input mechanism, eliminating the need for multiple single-value nodes.
