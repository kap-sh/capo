"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.status

ResourceStatus = TypedDict(
    "ResourceStatus",
    {
        "ec2": "capo_inspector2.types.status.Status",
        "ecr": "capo_inspector2.types.status.Status",
        "lambda": NotRequired["capo_inspector2.types.status.Status"],
        "lambda_code": NotRequired["capo_inspector2.types.status.Status"],
        "code_repository": NotRequired["capo_inspector2.types.status.Status"],
        "ami": NotRequired["capo_inspector2.types.status.Status"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> dict:
    out: dict = {}
    out["ec2"] = value["ec2"]
    out["ecr"] = value["ecr"]
    if "lambda" in value:
        out["lambda"] = value["lambda"]
    if "lambda_code" in value:
        out["lambdaCode"] = value["lambda_code"]
    if "code_repository" in value:
        out["codeRepository"] = value["code_repository"]
    if "ami" in value:
        out["ami"] = value["ami"]
    return out


def deserialize_json(data: dict) -> ResourceStatus:
    out: ResourceStatus = {}  # type: ignore[typeddict-item]
    if data.get("ec2") is not None:
        out["ec2"] = data["ec2"]
    else:
        out["ec2"] = ""
    if data.get("ecr") is not None:
        out["ecr"] = data["ecr"]
    else:
        out["ecr"] = ""
    if data.get("lambda") is not None:
        out["lambda"] = data["lambda"]
    if data.get("lambdaCode") is not None:
        out["lambda_code"] = data["lambdaCode"]
    if data.get("codeRepository") is not None:
        out["code_repository"] = data["codeRepository"]
    if data.get("ami") is not None:
        out["ami"] = data["ami"]
    return out
