"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListMicrovmImageBuildsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.architecture
    import capo_lambda_microvms.types.chipset
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.string


class ListMicrovmImageBuildsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>"""
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The unique identifier (ARN or ID) of the MicroVM image.</p>"""
    image_version: "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    """<p>The version of the MicroVM image to list builds for.</p>"""
    architecture: NotRequired["capo_lambda_microvms.types.architecture.Architecture"]
    """<p>Filters builds by target CPU architecture.</p>"""
    chipset: NotRequired["capo_lambda_microvms.types.chipset.Chipset"]
    """<p>Filters builds by target chipset.</p>"""
    chipset_generation: NotRequired[
        "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    ]
    """<p>Filters builds by target chipset generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrovmImageBuildsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMicrovmImageBuildsInput:
    out: ListMicrovmImageBuildsInput = {}  # type: ignore[typeddict-item]
    return out
