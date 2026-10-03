"""Generated from Smithy shape ``com.amazonaws.opensearch#AIMLOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.natural_language_query_generation_options_input
    import capo_opensearch.types.s3_vectors_engine
    import capo_opensearch.types.serverless_vector_acceleration


class AIMLOptionsInput(TypedDict, closed=True):
    natural_language_query_generation_options: NotRequired[
        "capo_opensearch.types.natural_language_query_generation_options_input.NaturalLanguageQueryGenerationOptionsInput"
    ]
    """<p>Container for parameters required for natural language query generation on the specified domain.</p>"""
    s3_vectors_engine: NotRequired[
        "capo_opensearch.types.s3_vectors_engine.S3VectorsEngine"
    ]
    """<p>Container for parameters required to enable S3 vectors engine features on the specified domain.</p>"""
    serverless_vector_acceleration: NotRequired[
        "capo_opensearch.types.serverless_vector_acceleration.ServerlessVectorAcceleration"
    ]
    """<p>Specifies whether to enable serverless vector acceleration for the domain. When enabled, provides <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gpu-acceleration-vector-index.html">GPU-accelerated</a> vector search capabilities for improved performance on vector workloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIMLOptionsInput) -> dict:
    out: dict = {}
    if "natural_language_query_generation_options" in value:
        import capo_opensearch.types.natural_language_query_generation_options_input

        out["NaturalLanguageQueryGenerationOptions"] = (
            capo_opensearch.types.natural_language_query_generation_options_input.serialize_json(
                value["natural_language_query_generation_options"]
            )
        )
    if "s3_vectors_engine" in value:
        import capo_opensearch.types.s3_vectors_engine

        out["S3VectorsEngine"] = capo_opensearch.types.s3_vectors_engine.serialize_json(
            value["s3_vectors_engine"]
        )
    if "serverless_vector_acceleration" in value:
        import capo_opensearch.types.serverless_vector_acceleration

        out["ServerlessVectorAcceleration"] = (
            capo_opensearch.types.serverless_vector_acceleration.serialize_json(
                value["serverless_vector_acceleration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AIMLOptionsInput:
    out: AIMLOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("NaturalLanguageQueryGenerationOptions") is not None:
        import capo_opensearch.types.natural_language_query_generation_options_input

        out["natural_language_query_generation_options"] = (
            capo_opensearch.types.natural_language_query_generation_options_input.deserialize_json(
                data["NaturalLanguageQueryGenerationOptions"]
            )
        )
    if data.get("S3VectorsEngine") is not None:
        import capo_opensearch.types.s3_vectors_engine

        out["s3_vectors_engine"] = (
            capo_opensearch.types.s3_vectors_engine.deserialize_json(
                data["S3VectorsEngine"]
            )
        )
    if data.get("ServerlessVectorAcceleration") is not None:
        import capo_opensearch.types.serverless_vector_acceleration

        out["serverless_vector_acceleration"] = (
            capo_opensearch.types.serverless_vector_acceleration.deserialize_json(
                data["ServerlessVectorAcceleration"]
            )
        )
    return out
