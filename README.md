# Procesamiento Digital de Imágenes con Python

**Autor:** Dr. Mitchell Ángel Gómez Ortega
**Institución:** Universidad Politécnica de Pachuca
**Asignatura:** Sistemas de Visión Artificial

---

## Descripción

Este repositorio contiene notebooks desarrollados para la asignatura **Sistemas de Visión Artificial**, donde se presentan conceptos fundamentales del procesamiento digital de imágenes utilizando Python y bibliotecas especializadas como **NumPy**, **Matplotlib** y **Scikit-Image**.

El material está diseñado para introducir al estudiante en la representación, manipulación, segmentación y mejoramiento de imágenes digitales mediante ejemplos prácticos implementados en Jupyter Notebook.

---

## Contenido

### Notebook 1: Introducción al Procesamiento Digital de Imágenes

En este notebook se presentan los conceptos básicos para comenzar a trabajar con imágenes digitales utilizando la biblioteca **Scikit-Image**.

**Temas abordados:**

* Instalación de Scikit-Image.
* Instalación de bibliotecas complementarias.
* Verificación de dependencias.
* Carga de imágenes incluidas en Scikit-Image.
* Visualización de imágenes.
* Diferencias entre imágenes en escala de grises y color.
* Representación digital de una imagen.

---

### Notebook 2: Imágenes con NumPy

Introducción al uso de arreglos NumPy para manipular imágenes digitales.

**Temas abordados:**

* Conversión de imágenes RGB a escala de grises.
* Visualización de valores numéricos de una imagen.
* Tipo de dato de una imagen.
* Manipulación de arreglos multidimensionales.
* Extracción del canal rojo.
* Separación de canales RGB.
* Volteo vertical de imágenes (`flipud`).
* Volteo horizontal de imágenes (`fliplr`).

---

### Notebook 2.1: Ecualización de Histogramas

Introducción a la técnica de ecualización de histogramas para mejorar el contraste.

**Temas abordados:**

* Concepto de histograma.
* Ecualización de histogramas.
* Comparación entre imagen original y ecualizada.
* Comparación de histogramas antes y después del procesamiento.

---

### Notebook 3: Thresholding (Umbralización)

Introducción a técnicas de segmentación basadas en umbrales.

**Temas abordados:**

* Umbralización binaria.
* Umbralización invertida.
* Comparación de algoritmos mediante `try_all_threshold()`.
* Método automático de Otsu.
* Umbralización local.
* Aplicaciones de segmentación de imágenes.

---

### Notebook 4: Filtering

Aplicación de filtros espaciales para análisis y mejoramiento de imágenes.

**Temas abordados:**

* Filtrado de imágenes.
* Comparación entre imagen original y filtrada.
* Detección de bordes utilizando el operador Sobel.
* Suavizado mediante filtro Gaussiano.
* Aplicación de filtros sobre imágenes RGB.
* Análisis visual de resultados.

---

### Notebook 5: Histogram Equalization

Aplicación de técnicas de mejoramiento de contraste sobre distintos tipos de imágenes.

**Temas abordados:**

* Lectura y visualización de imágenes.
* Histogramas de intensidad.
* Mejoramiento de contraste.
* Ecualización de histogramas.
* Aplicaciones en imágenes médicas.
* Aplicaciones en imágenes aéreas.
* CLAHE (Contrast Limited Adaptive Histogram Equalization).

---

## Requisitos

Se recomienda utilizar Python 3.10 o superior.

Instalación de dependencias:

```bash
pip install numpy matplotlib scikit-image opencv-python pillow
```

---

## Bibliotecas Utilizadas

* NumPy
* Matplotlib
* Scikit-Image
* OpenCV
* Pillow

---

## Objetivo General

Desarrollar habilidades básicas en procesamiento digital de imágenes mediante el uso de Python, comprendiendo la representación de imágenes, su manipulación, segmentación y mejoramiento para aplicaciones de visión artificial.

---

## Licencia

Material desarrollado con fines académicos para la asignatura **Sistemas de Visión Artificial** de la **Universidad Politécnica de Pachuca**.

© Dr. Mitchell Ángel Gómez Ortega
