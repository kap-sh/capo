"""Generated from Smithy shape ``com.amazonaws.batch#NetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.assign_public_ip


class NetworkConfiguration(TypedDict, closed=True):
    assign_public_ip: NotRequired["capo_batch.types.assign_public_ip.AssignPublicIp"]
    """<p>Indicates whether the job has a public IP address. For a job that's running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Amazon ECS task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. The default value is "<code>DISABLED</code>".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "assign_public_ip" in value:
        import capo_batch.types.assign_public_ip

        out["assignPublicIp"] = capo_batch.types.assign_public_ip.serialize_json(
            value["assign_public_ip"]
        )
    return out


def deserialize_json(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("assignPublicIp") is not None:
        import capo_batch.types.assign_public_ip

        out["assign_public_ip"] = capo_batch.types.assign_public_ip.deserialize_json(
            data["assignPublicIp"]
        )
    return out
