"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsGrantConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.grantee_principal
    import capo_accessanalyzer.types.issuing_account
    import capo_accessanalyzer.types.kms_grant_constraints
    import capo_accessanalyzer.types.kms_grant_operations_list
    import capo_accessanalyzer.types.retiring_principal


class KmsGrantConfiguration(TypedDict, closed=True):
    operations: (
        "capo_accessanalyzer.types.kms_grant_operations_list.KmsGrantOperationsList"
    )
    """<p>A list of operations that the grant permits.</p>"""
    grantee_principal: "capo_accessanalyzer.types.grantee_principal.GranteePrincipal"
    """<p>The principal that is given permission to perform the operations that the grant permits.</p>"""
    retiring_principal: NotRequired[
        "capo_accessanalyzer.types.retiring_principal.RetiringPrincipal"
    ]
    """<p>The principal that is given permission to retire the grant by using <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html">RetireGrant</a> operation.</p>"""
    constraints: NotRequired[
        "capo_accessanalyzer.types.kms_grant_constraints.KmsGrantConstraints"
    ]
    """<p>Use this structure to propose allowing <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations">cryptographic operations</a> in the grant only when the operation request includes the specified <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context">encryption context</a>.</p>"""
    issuing_account: "capo_accessanalyzer.types.issuing_account.IssuingAccount"
    """<p> The Amazon Web Services account under which the grant was issued. The account is used to propose KMS grants issued by accounts other than the owner of the key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsGrantConfiguration) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.kms_grant_operations_list

    out["operations"] = (
        capo_accessanalyzer.types.kms_grant_operations_list.serialize_json(
            value["operations"]
        )
    )
    out["granteePrincipal"] = value["grantee_principal"]
    if "retiring_principal" in value:
        out["retiringPrincipal"] = value["retiring_principal"]
    if "constraints" in value:
        import capo_accessanalyzer.types.kms_grant_constraints

        out["constraints"] = (
            capo_accessanalyzer.types.kms_grant_constraints.serialize_json(
                value["constraints"]
            )
        )
    out["issuingAccount"] = value["issuing_account"]
    return out


def deserialize_json(data: dict) -> KmsGrantConfiguration:
    out: KmsGrantConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("operations") is not None:
        import capo_accessanalyzer.types.kms_grant_operations_list

        out["operations"] = (
            capo_accessanalyzer.types.kms_grant_operations_list.deserialize_json(
                data["operations"]
            )
        )
    else:
        raise DeserializationError("KmsGrantConfiguration.operations required")
    if data.get("granteePrincipal") is not None:
        out["grantee_principal"] = data["granteePrincipal"]
    else:
        raise DeserializationError("KmsGrantConfiguration.grantee_principal required")
    if data.get("retiringPrincipal") is not None:
        out["retiring_principal"] = data["retiringPrincipal"]
    if data.get("constraints") is not None:
        import capo_accessanalyzer.types.kms_grant_constraints

        out["constraints"] = (
            capo_accessanalyzer.types.kms_grant_constraints.deserialize_json(
                data["constraints"]
            )
        )
    if data.get("issuingAccount") is not None:
        out["issuing_account"] = data["issuingAccount"]
    else:
        raise DeserializationError("KmsGrantConfiguration.issuing_account required")
    return out
