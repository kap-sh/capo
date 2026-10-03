"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridAdministratorAccountUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.secret_arn


class HybridAdministratorAccountUpdate(TypedDict, closed=True):
    secret_arn: "capo_directory_service.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials for the AD administrator user, and enables hybrid domain controllers to join the managed AD domain. For example:</p> <p> <code> {"customerAdAdminDomainUsername":"carlos_salazar","customerAdAdminDomainPassword":"ExamplePassword123!"}. </code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridAdministratorAccountUpdate) -> dict:
    out: dict = {}
    out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridAdministratorAccountUpdate:
    out: HybridAdministratorAccountUpdate = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError(
            "HybridAdministratorAccountUpdate.secret_arn required"
        )
    return out
