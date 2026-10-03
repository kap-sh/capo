"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.accelerator_name
    import capo_deadline.types.accelerator_runtime


class AcceleratorSelection(TypedDict, closed=True):
    name: "capo_deadline.types.accelerator_name.AcceleratorName"
    """<p>The name of the chip used by the GPU accelerator.</p> <p>The available GPU accelerators are:</p> <ul> <li> <p> <code>t4</code> - NVIDIA T4 Tensor Core GPU (16 GiB memory)</p> </li> <li> <p> <code>a10g</code> - NVIDIA A10G Tensor Core GPU (24 GiB memory)</p> </li> <li> <p> <code>l4</code> - NVIDIA L4 Tensor Core GPU (24 GiB memory)</p> </li> <li> <p> <code>l40s</code> - NVIDIA L40S Tensor Core GPU (48 GiB memory)</p> </li> <li> <p> <code>rtx-pro-server-6000</code> - NVIDIA RTX PRO Server 6000 GPU (96 GiB memory)</p> </li> </ul>"""
    runtime: "capo_deadline.types.accelerator_runtime.AcceleratorRuntime"
    """<p>Specifies the runtime driver to use for the GPU accelerator. You must use the same runtime for all GPUs in a fleet. </p> <p>You can choose from the following runtimes:</p> <ul> <li> <p> <code>latest</code> - Use the latest runtime available for the chip. If you specify <code>latest</code> and a new version of the runtime is released, the new version of the runtime is used.</p> </li> <li> <p> <code>grid:r580</code> - <a href="https://docs.nvidia.com/vgpu/19.0/index.html">NVIDIA vGPU software 19</a> </p> </li> <li> <p> <code>grid:r570</code> - <a href="https://docs.nvidia.com/vgpu/18.0/index.html">NVIDIA vGPU software 18</a> </p> </li> <li> <p> <code>grid:r535</code> - <a href="https://docs.nvidia.com/vgpu/16.0/index.html">NVIDIA vGPU software 16</a> </p> </li> </ul> <p>If you don't specify a runtime, Amazon Web Services Deadline Cloud uses <code>latest</code> as the default. However, if you have multiple accelerators and specify <code>latest</code> for some and leave others blank, Amazon Web Services Deadline Cloud raises an exception.</p> <important> <p>Not all runtimes are compatible with all accelerator types:</p> <ul> <li> <p> <code>t4</code> and <code>a10g</code>: Support all runtimes (<code>grid:r580</code>, <code>grid:r570</code>, <code>grid:r535</code>)</p> </li> <li> <p> <code>l4</code> and <code>l40s</code>: Only support <code>grid:r570</code> and newer</p> </li> <li> <p> <code>rtx-pro-server-6000</code>: Only supports <code>grid:r580</code> </p> </li> </ul> <p>All accelerators in a fleet must use the same runtime version. You cannot mix different runtime versions within a single fleet.</p> </important> <note> <p>When you specify <code>latest</code>, it resolves to <code>grid:r580</code> for all currently supported accelerators.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorSelection) -> dict:
    out: dict = {}
    import capo_deadline.types.accelerator_name

    out["name"] = capo_deadline.types.accelerator_name.serialize_json(value["name"])
    out["runtime"] = value.get("runtime", "latest")
    return out


def deserialize_json(data: dict) -> AcceleratorSelection:
    out: AcceleratorSelection = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_deadline.types.accelerator_name

        out["name"] = capo_deadline.types.accelerator_name.deserialize_json(
            data["name"]
        )
    else:
        raise DeserializationError("AcceleratorSelection.name required")
    if data.get("runtime") is not None:
        out["runtime"] = data["runtime"]
    else:
        out["runtime"] = "latest"
    return out
