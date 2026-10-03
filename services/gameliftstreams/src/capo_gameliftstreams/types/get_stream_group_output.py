"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#GetStreamGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_gameliftstreams.types.arn_list
    import capo_gameliftstreams.types.default_application
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.id
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.location_states
    import capo_gameliftstreams.types.stream_class
    import capo_gameliftstreams.types.stream_group_status
    import capo_gameliftstreams.types.stream_group_status_reason


class GetStreamGroupOutput(TypedDict, closed=True):
    arn: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that is assigned to the stream group resource and that uniquely identifies the group across all Amazon Web Services Regions. Format is <code>arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamgroup/[resource ID]</code>.</p>"""
    description: NotRequired["capo_gameliftstreams.types.description.Description"]
    """<p>A descriptive label for the stream group.</p>"""
    default_application: NotRequired[
        "capo_gameliftstreams.types.default_application.DefaultApplication"
    ]
    """<p>The default Amazon GameLift Streams application that is associated with this stream group.</p>"""
    location_states: NotRequired[
        "capo_gameliftstreams.types.location_states.LocationStates"
    ]
    """<p>This value is the set of locations, including their name, current status, and capacities. </p> <p>A location can be in one of the following states:</p> <ul> <li> <p> <code>ACTIVATING</code>: Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.</p> </li> <li> <p> <code>ACTIVE</code>: The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.</p> </li> <li> <p> <code>ERROR</code>: Amazon GameLift Streams failed to set up this location. The <code>StatusReason</code> field describes the error. You can remove this location and try to add it again.</p> </li> <li> <p> <code>REMOVING</code>: Amazon GameLift Streams is working to remove this location. This will release all provisioned capacity for this location in this stream group.</p> </li> </ul>"""
    stream_class: NotRequired["capo_gameliftstreams.types.stream_class.StreamClass"]
    """<p>The target stream quality for the stream group.</p> <p>A stream class can be one of the following:</p> <ul> <li> <p> <b> <code>gen6n_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra_win2022</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium</code> (NVIDIA, medium)</b> Supports applications with moderate 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 4 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small</code> (NVIDIA, small)</b> Supports applications with lightweight 3D scene complexity and low CPU usage. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 1 vCPUs, 4 GB RAM, 2 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 12 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium_win2022</code> (NVIDIA, medium)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small_win2022</code> (NVIDIA, small)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 3 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_ultra</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> </ul>"""
    id: NotRequired["capo_gameliftstreams.types.id.Id"]
    """<p>A unique ID value that is assigned to the resource when it's created. Format example: <code>sg-1AB2C3De4</code>.</p>"""
    status: NotRequired[
        "capo_gameliftstreams.types.stream_group_status.StreamGroupStatus"
    ]
    """<p>The current status of the stream group resource. Possible statuses include the following:</p> <ul> <li> <p> <code>ACTIVATING</code>: The stream group is deploying and isn't ready to host streams. </p> </li> <li> <p> <code>ACTIVE</code>: The stream group is ready to host streams. </p> </li> <li> <p> <code>ACTIVE_WITH_ERRORS</code>: One or more locations in the stream group are in an error state. Verify the details of individual locations and remove any locations which are in error. </p> </li> <li> <p> <code>DELETING</code>: Amazon GameLift Streams is in the process of deleting the stream group. </p> </li> <li> <p> <code>ERROR</code>: An error occurred when the stream group deployed. See <code>StatusReason</code> (returned by <code>CreateStreamGroup</code>, <code>GetStreamGroup</code>, and <code>UpdateStreamGroup</code>) for more information. </p> </li> <li> <p> <code>EXPIRED</code>: The stream group is expired and can no longer host streams. This typically occurs when a stream group is 365 days old, as indicated by the value of <code>ExpiresAt</code>. Create a new stream group to resume streaming capabilities. </p> </li> <li> <p> <code>UPDATING_LOCATIONS</code>: One or more locations in the stream group are in the process of updating (either activating or deleting). </p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_gameliftstreams.types.stream_group_status_reason.StreamGroupStatusReason"
    ]
    """<p> A short description of the reason that the stream group is in <code>ERROR</code> status. The possible reasons can be one of the following: </p> <ul> <li> <p> <code>internalError</code>: The request can't process right now because of an issue with the server. Try again later.</p> </li> <li> <p> <code>noAvailableInstances</code>: Amazon GameLift Streams does not currently have enough available capacity to fulfill your request. Wait a few minutes and retry the request as capacity can shift frequently. You can also try to make the request using a different stream class or in another region.</p> </li> </ul>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p>The time at which this stream group expires. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC). After this time, you will no longer be able to update this stream group or use it to start stream sessions. Only Get and Delete operations will work on an expired stream group.</p>"""
    associated_applications: NotRequired["capo_gameliftstreams.types.arn_list.ArnList"]
    """<p> A set of applications that this stream group is associated to. You can stream any of these applications by using this stream group. </p> <p>This value is a set of <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Names (ARNs)</a> that uniquely identify application resources. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamGroupOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "default_application" in value:
        import capo_gameliftstreams.types.default_application

        out["DefaultApplication"] = (
            capo_gameliftstreams.types.default_application.serialize_json(
                value["default_application"]
            )
        )
    if "location_states" in value:
        import capo_gameliftstreams.types.location_states

        out["LocationStates"] = (
            capo_gameliftstreams.types.location_states.serialize_json(
                value["location_states"]
            )
        )
    if "stream_class" in value:
        import capo_gameliftstreams.types.stream_class

        out["StreamClass"] = capo_gameliftstreams.types.stream_class.serialize_json(
            value["stream_class"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_gameliftstreams.types.stream_group_status

        out["Status"] = capo_gameliftstreams.types.stream_group_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import capo_gameliftstreams.types.stream_group_status_reason

        out["StatusReason"] = (
            capo_gameliftstreams.types.stream_group_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "last_updated_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            capo_gameliftstreams.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "created_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["CreatedAt"] = capo_gameliftstreams.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "expires_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["ExpiresAt"] = capo_gameliftstreams.types._prelude.timestamp.serialize_json(
            value["expires_at"]
        )
    if "associated_applications" in value:
        import capo_gameliftstreams.types.arn_list

        out["AssociatedApplications"] = (
            capo_gameliftstreams.types.arn_list.serialize_json(
                value["associated_applications"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetStreamGroupOutput:
    out: GetStreamGroupOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetStreamGroupOutput.arn required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultApplication") is not None:
        import capo_gameliftstreams.types.default_application

        out["default_application"] = (
            capo_gameliftstreams.types.default_application.deserialize_json(
                data["DefaultApplication"]
            )
        )
    if data.get("LocationStates") is not None:
        import capo_gameliftstreams.types.location_states

        out["location_states"] = (
            capo_gameliftstreams.types.location_states.deserialize_json(
                data["LocationStates"]
            )
        )
    if data.get("StreamClass") is not None:
        import capo_gameliftstreams.types.stream_class

        out["stream_class"] = capo_gameliftstreams.types.stream_class.deserialize_json(
            data["StreamClass"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_gameliftstreams.types.stream_group_status

        out["status"] = capo_gameliftstreams.types.stream_group_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        import capo_gameliftstreams.types.stream_group_status_reason

        out["status_reason"] = (
            capo_gameliftstreams.types.stream_group_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["created_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("ExpiresAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["expires_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["ExpiresAt"]
            )
        )
    if data.get("AssociatedApplications") is not None:
        import capo_gameliftstreams.types.arn_list

        out["associated_applications"] = (
            capo_gameliftstreams.types.arn_list.deserialize_json(
                data["AssociatedApplications"]
            )
        )
    return out
