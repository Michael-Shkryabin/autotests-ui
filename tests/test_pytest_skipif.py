import pytest

SYSTEM_VERSION = "V1.2.0"


@pytest.mark.skipif(
    SYSTEM_VERSION == "V1.3.0",  # SYSTEM_VERSION == "V1.3.0" => False
    reason="Тест не может быть запущен на версии системы V1.3.0"
)
def test_system_version_valid():
    ...


@pytest.mark.skipif(
    SYSTEM_VERSION == "V1.2.0",  # SYSTEM_VERSION == "V1.2.0" => True
    reason="Тест не может быть запущен на версии системы V1.2.0"
)
def test_system_version_invalid():
    ...
