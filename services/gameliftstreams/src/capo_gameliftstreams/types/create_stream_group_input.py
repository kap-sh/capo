"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#CreateStreamGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.client_token
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.location_configurations
    import capo_gameliftstreams.types.stream_class
    import capo_gameliftstreams.types.tags


class CreateStreamGroupInput(TypedDict, closed=True):
    description: "capo_gameliftstreams.types.description.Description"
    """<p>A descriptive label for the stream group.</p>"""
    stream_class: "capo_gameliftstreams.types.stream_class.StreamClass"
    """<p>The target stream quality for sessions that are hosted in this stream group. Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available: </p> <p>A stream class can be one of the following:</p> <ul> <li> <p> <b> <code>gen6n_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra_win2022</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium</code> (NVIDIA, medium)</b> Supports applications with moderate 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 4 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small</code> (NVIDIA, small)</b> Supports applications with lightweight 3D scene complexity and low CPU usage. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 1 vCPUs, 4 GB RAM, 2 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 12 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium_win2022</code> (NVIDIA, medium)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small_win2022</code> (NVIDIA, small)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 3 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_ultra</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> </ul>"""
    default_application_identifier: NotRequired[
        "capo_gameliftstreams.types.identifier.Identifier"
    ]
    """<p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>If you do not link an application when you create a stream group, you will need to link one later, before you can start streaming, using <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html">AssociateApplications</a>.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""
    location_configurations: NotRequired[
        "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
    ]
    """<p> A set of one or more locations and the streaming capacity for each location. </p>"""
    tags: NotRequired["capo_gameliftstreams.types.tags.Tags"]
    """<p>A list of labels to assign to the new stream group resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html">TagResource</a> to add tags, <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html">UntagResource</a> to remove tags, and <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to view tags on existing resources.</p>"""
    client_token: NotRequired["capo_gameliftstreams.types.client_token.ClientToken"]
    """<p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamGroupInput) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    import capo_gameliftstreams.types.stream_class

    out["StreamClass"] = capo_gameliftstreams.types.stream_class.serialize_json(
        value["stream_class"]
    )
    if "default_application_identifier" in value:
        out["DefaultApplicationIdentifier"] = value["default_application_identifier"]
    if "location_configurations" in value:
        import capo_gameliftstreams.types.location_configurations

        out["LocationConfigurations"] = (
            capo_gameliftstreams.types.location_configurations.serialize_json(
                value["location_configurations"]
            )
        )
    if "tags" in value:
        import capo_gameliftstreams.types.tags

        out["Tags"] = capo_gameliftstreams.types.tags.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateStreamGroupInput:
    out: CreateStreamGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateStreamGroupInput.description required")
    if data.get("StreamClass") is not None:
        import capo_gameliftstreams.types.stream_class

        out["stream_class"] = capo_gameliftstreams.types.stream_class.deserialize_json(
            data["StreamClass"]
        )
    else:
        raise DeserializationError("CreateStreamGroupInput.stream_class required")
    if data.get("DefaultApplicationIdentifier") is not None:
        out["default_application_identifier"] = data["DefaultApplicationIdentifier"]
    if data.get("LocationConfigurations") is not None:
        import capo_gameliftstreams.types.location_configurations

        out["location_configurations"] = (
            capo_gameliftstreams.types.location_configurations.deserialize_json(
                data["LocationConfigurations"]
            )
        )
    if data.get("Tags") is not None:
        import capo_gameliftstreams.types.tags

        out["tags"] = capo_gameliftstreams.types.tags.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
