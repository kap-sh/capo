"""Tests for ``apply_label`` — strips a URI-template placeholder when the
runtime value is already embedded as a whole host label or path segment
of the resolved endpoint URL."""

from __future__ import annotations

from capo_supportauthz._rule_engine._endpoint_runtime import apply_label


def test_strips_when_value_is_host_label() -> None:
    # Rule engine put bucket into the host; url has the placeholder appended
    # by ``endpoint.url.rstrip("/") + uri_template``.
    assert (
        apply_label("https://bucket.example.org/{Bucket}", "{Bucket}", "bucket")
        == "https://bucket.example.org"
    )


def test_strips_when_value_is_path_segment() -> None:
    assert (
        apply_label("https://example.org/bucket/{Bucket}", "{Bucket}", "bucket")
        == "https://example.org/bucket"
    )


def test_strips_keeps_trailing_path_after_placeholder() -> None:
    assert (
        apply_label("https://example.org/bucket/{Bucket}/key", "{Bucket}", "bucket")
        == "https://example.org/bucket/key"
    )


def test_strips_trailing_slash_after_strip() -> None:
    assert (
        apply_label("https://example.org/bucket/{Bucket}/", "{Bucket}", "bucket")
        == "https://example.org/bucket"
    )


def test_substitutes_when_no_match() -> None:
    assert (
        apply_label("https://example.org/{Bucket}", "{Bucket}", "mybucket")
        == "https://example.org/mybucket"
    )


def test_substitutes_percent_encodes_non_match() -> None:
    assert (
        apply_label("https://example.org/{Bucket}", "{Bucket}", "my bucket")
        == "https://example.org/my%20bucket"
    )


def test_partial_token_not_stripped() -> None:
    # "bucket" is a substring of "my-bucket" but not a whole part.
    assert (
        apply_label("https://my-bucket.example.org/{Bucket}", "{Bucket}", "bucket")
        == "https://my-bucket.example.org/bucket"
    )


def test_case_sensitive() -> None:
    assert (
        apply_label("https://Bucket.example.org/{Bucket}", "{Bucket}", "bucket")
        == "https://Bucket.example.org/bucket"
    )


def test_empty_value_substitutes() -> None:
    assert (
        apply_label("https://example.org/{Bucket}", "{Bucket}", "")
        == "https://example.org/"
    )


def test_placeholder_absent_returns_unchanged() -> None:
    assert (
        apply_label("https://bucket.example.org", "{Bucket}", "bucket")
        == "https://bucket.example.org"
    )


def test_ipv6_authority_safe() -> None:
    # No host label should match; value gets substituted.
    assert (
        apply_label("https://[::1]/{Bucket}", "{Bucket}", "bucket")
        == "https://[::1]/bucket"
    )


def test_strip_collapses_double_slash_in_path() -> None:
    # Placeholder mid-path leaves `//` after removal; must collapse.
    assert (
        apply_label("https://example.org/bucket/{Bucket}/sub", "{Bucket}", "bucket")
        == "https://example.org/bucket/sub"
    )


def test_port_bearing_authority_strips_host_label() -> None:
    assert (
        apply_label("https://bucket.example.org:9000/{Bucket}", "{Bucket}", "bucket")
        == "https://bucket.example.org:9000"
    )


def test_query_string_placeholder_with_host_label_match_substitutes() -> None:
    # Value "bucket" matches host label, but placeholder lives only in
    # the query string — strip must NOT fire.
    assert (
        apply_label("https://bucket.example.org/?key={Bucket}", "{Bucket}", "bucket")
        == "https://bucket.example.org/?key=bucket"
    )
