    # Validación por clave secreta
    if request_data.get('secret') != secret_key:
        logger.warning('Intento de webhook no autorizado')
        return False
    
    return True
except Exception as e:
    logger.error(f'Error en validación de webhook: {e}')
    return False
