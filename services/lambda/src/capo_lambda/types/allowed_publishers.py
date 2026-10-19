"""Generated from Smithy shape ``com.amazonaws.lambda#AllowedPublishers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.signing_profile_version_arns


class AllowedPublishers(TypedDict, closed=True):
    signing_profile_version_arns: (
        "capo_lambda.types.signing_profile_version_arns.SigningProfileVersionArns"
    )
    """<p>The Amazon Resource Name (ARN) for each of the signing profiles. A signing profile defines a trusted user who can sign a code package. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedPublishers) -> dict:
    out: dict = {}
    import capo_lambda.types.signing_profile_version_arns

    out["SigningProfileVersionArns"] = (
        capo_lambda.types.signing_profile_version_arns.serialize_json(
            value["signing_profile_version_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> AllowedPublishers:
    out: AllowedPublishers = {}  # type: ignore[typeddict-item]
    if data.get("SigningProfileVersionArns") is not None:
        import capo_lambda.types.signing_profile_version_arns

        out["signing_profile_version_arns"] = (
            capo_lambda.types.signing_profile_version_arns.deserialize_json(
                data["SigningProfileVersionArns"]
            )
        )
    else:
        out["signing_profile_version_arns"] = []
    return out
