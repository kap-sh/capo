"""Generated from Smithy shape ``com.amazonaws.inspector2#AutoEnable``."""

from typing_extensions import NotRequired, TypedDict

AutoEnable = TypedDict(
    "AutoEnable",
    {
        "ec2": "bool",
        "ecr": "bool",
        "lambda": NotRequired["bool"],
        "lambda_code": NotRequired["bool"],
        "code_repository": NotRequired["bool"],
        "ami": NotRequired["bool"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: AutoEnable) -> dict:
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


def deserialize_json(data: dict) -> AutoEnable:
    out: AutoEnable = {}  # type: ignore[typeddict-item]
    if data.get("ec2") is not None:
        out["ec2"] = data["ec2"]
    else:
        out["ec2"] = False
    if data.get("ecr") is not None:
        out["ecr"] = data["ecr"]
    else:
        out["ecr"] = False
    if data.get("lambda") is not None:
        out["lambda"] = data["lambda"]
    if data.get("lambdaCode") is not None:
        out["lambda_code"] = data["lambdaCode"]
    if data.get("codeRepository") is not None:
        out["code_repository"] = data["codeRepository"]
    if data.get("ami") is not None:
        out["ami"] = data["ami"]
    return out
