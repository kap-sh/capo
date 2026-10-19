"""Generated from Smithy shape ``com.amazonaws.ecr#SigningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.signing_rule_list


class SigningConfiguration(TypedDict, closed=True):
    rules: "capo_ecr.types.signing_rule_list.SigningRuleList"
    """<p>A list of signing rules. Each rule defines a signing profile and optional repository filters that determine which images are automatically signed. Maximum of 10 rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningConfiguration) -> dict:
    out: dict = {}
    import capo_ecr.types.signing_rule_list

    out["rules"] = capo_ecr.types.signing_rule_list.serialize_aws_json_1_1(
        value["rules"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SigningConfiguration:
    out: SigningConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_ecr.types.signing_rule_list

        out["rules"] = capo_ecr.types.signing_rule_list.deserialize_aws_json_1_1(
            data["rules"]
        )
    else:
        out["rules"] = []
    return out
