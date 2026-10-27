"""Generated from Smithy shape ``com.amazonaws.deadline#CopyJobTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.job_template_type


class CopyJobTemplateResponse(TypedDict, closed=True):
    template_type: "capo_deadline.types.job_template_type.JobTemplateType"
    """The format of the job template, either <code>JSON</code> or <code>YAML</code>."""


# --- restJson1 ser/de ---
def serialize_json(value: CopyJobTemplateResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.job_template_type

    out["templateType"] = capo_deadline.types.job_template_type.serialize_json(
        value["template_type"]
    )
    return out


def deserialize_json(data: dict) -> CopyJobTemplateResponse:
    out: CopyJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("templateType") is not None:
        import capo_deadline.types.job_template_type

        out["template_type"] = capo_deadline.types.job_template_type.deserialize_json(
            data["templateType"]
        )
    else:
        import typing

        out["template_type"] = typing.cast(
            "capo_deadline.types.job_template_type.JobTemplateType", ""
        )
    return out
