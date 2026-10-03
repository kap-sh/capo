"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GeneratedPolicy``."""

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError


class GeneratedPolicy(TypedDict, closed=True):
    policy: "str"
    """<p>The text to use as the content for the new policy. The policy is created using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html">CreatePolicy</a> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedPolicy) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GeneratedPolicy:
    out: GeneratedPolicy = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("GeneratedPolicy.policy required")
    return out
