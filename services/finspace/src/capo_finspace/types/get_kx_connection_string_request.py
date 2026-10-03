"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxConnectionStringRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.id_type
    import capo_finspace.types.kx_cluster_name
    import capo_finspace.types.kx_user_arn


class GetKxConnectionStringRequest(TypedDict, closed=True):
    user_arn: "capo_finspace.types.kx_user_arn.KxUserArn"
    """<p> The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>"""
    environment_id: "capo_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName"
    """<p>A name of the kdb cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxConnectionStringRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxConnectionStringRequest:
    out: GetKxConnectionStringRequest = {}  # type: ignore[typeddict-item]
    return out
