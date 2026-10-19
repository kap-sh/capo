"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartTestExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.test_execution_api_mode
    import capo_lex_models_v2.types.test_execution_modality
    import capo_lex_models_v2.types.test_execution_target


class StartTestExecutionRequest(TypedDict, closed=True):
    test_set_id: "capo_lex_models_v2.types.id.Id"
    """<p>The test set Id for the test set execution.</p>"""
    target: "capo_lex_models_v2.types.test_execution_target.TestExecutionTarget"
    """<p>The target bot for the test set execution.</p>"""
    api_mode: "capo_lex_models_v2.types.test_execution_api_mode.TestExecutionApiMode"
    """<p>Indicates whether we use streaming or non-streaming APIs for the test set execution. For streaming, StartConversation Runtime API is used. Whereas, for non-streaming, RecognizeUtterance and RecognizeText Amazon Lex Runtime API are used.</p>"""
    test_execution_modality: NotRequired[
        "capo_lex_models_v2.types.test_execution_modality.TestExecutionModality"
    ]
    """<p>Indicates whether audio or text is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestExecutionRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.test_execution_target

    out["target"] = capo_lex_models_v2.types.test_execution_target.serialize_json(
        value["target"]
    )
    import capo_lex_models_v2.types.test_execution_api_mode

    out["apiMode"] = capo_lex_models_v2.types.test_execution_api_mode.serialize_json(
        value["api_mode"]
    )
    if "test_execution_modality" in value:
        import capo_lex_models_v2.types.test_execution_modality

        out["testExecutionModality"] = (
            capo_lex_models_v2.types.test_execution_modality.serialize_json(
                value["test_execution_modality"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartTestExecutionRequest:
    out: StartTestExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("target") is not None:
        import capo_lex_models_v2.types.test_execution_target

        out["target"] = capo_lex_models_v2.types.test_execution_target.deserialize_json(
            data["target"]
        )
    else:
        raise DeserializationError("StartTestExecutionRequest.target required")
    if data.get("apiMode") is not None:
        import capo_lex_models_v2.types.test_execution_api_mode

        out["api_mode"] = (
            capo_lex_models_v2.types.test_execution_api_mode.deserialize_json(
                data["apiMode"]
            )
        )
    else:
        import typing

        out["api_mode"] = typing.cast(
            "capo_lex_models_v2.types.test_execution_api_mode.TestExecutionApiMode", ""
        )
    if data.get("testExecutionModality") is not None:
        import capo_lex_models_v2.types.test_execution_modality

        out["test_execution_modality"] = (
            capo_lex_models_v2.types.test_execution_modality.deserialize_json(
                data["testExecutionModality"]
            )
        )
    return out
