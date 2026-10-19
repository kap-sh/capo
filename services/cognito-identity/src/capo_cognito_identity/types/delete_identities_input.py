"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DeleteIdentitiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id_list


class DeleteIdentitiesInput(TypedDict, closed=True):
    identity_ids_to_delete: (
        "capo_cognito_identity.types.identity_id_list.IdentityIdList"
    )
    """<p>A list of 1-60 identities that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentitiesInput) -> dict:
    out: dict = {}
    import capo_cognito_identity.types.identity_id_list

    out["IdentityIdsToDelete"] = (
        capo_cognito_identity.types.identity_id_list.serialize_aws_json_1_1(
            value["identity_ids_to_delete"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentitiesInput:
    out: DeleteIdentitiesInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityIdsToDelete") is not None:
        import capo_cognito_identity.types.identity_id_list

        out["identity_ids_to_delete"] = (
            capo_cognito_identity.types.identity_id_list.deserialize_aws_json_1_1(
                data["IdentityIdsToDelete"]
            )
        )
    else:
        out["identity_ids_to_delete"] = []
    return out
