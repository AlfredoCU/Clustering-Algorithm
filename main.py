#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 01:04:19 2020

@author: alfredocu
"""

# Importar librerias.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster, datasets, mixture
from sklearn.preprocessing import StandardScaler

# Crear datos de prueba.
np.random.seed(0)
n_samples = 1500
X = 6*[None]

# Circulos concentricos.
xtemp, _ = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
X[0] = StandardScaler().fit_transform(xtemp)

# Lunas.
xtemp, _ = datasets.make_moons(n_samples=n_samples, noise=.05)
X[1] = StandardScaler().fit_transform(xtemp)

# Blobs.
xtemp, _ = datasets.make_blobs(n_samples=n_samples, random_state=8)
X[2] = StandardScaler().fit_transform(xtemp)

# Plano sin agrupaciones.
xtemp = np.random.rand(n_samples, 2)
X[3] = StandardScaler().fit_transform(xtemp)

# Blobs con deformación anisotropica.
xtemp, _ = datasets.make_blobs(n_samples=n_samples, random_state=170)
xtemp = np.dot(xtemp, [[0.6, -0.6], [-0.4, 0.8]])
X[4] = StandardScaler().fit_transform(xtemp)

# Blobs con varias varianzas.
xtemp, _ = datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=142)
X[5] = StandardScaler().fit_transform(xtemp)

# Números de clusters.
classes = [2, 2, 3, 3, 3, 3]

# Dibujar.
plt.figure(figsize=(27,9))
for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    ax.scatter(X[i][:,0], X[i][:,1])

plt.savefig("Grafics.eps", format="eps")

# =============================================================================

y = []
for c, x in zip(classes, X):
    model = cluster.KMeans(n_clusters=c)
    model.fit(x)
    if hasattr(model, "labels_"):
        y.append(model.labels_.astype(np.int))
    else:
        y.append(model.predict(x))
        
fig = plt.figure(figsize=(27, 9))
fig.suptitle("Kmeans", fontsize=48)
for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    ax.scatter(X[i][:,0], X[i][:,1], c=y[i])
    
plt.savefig("Kmeans.eps", format="eps")

# =============================================================================

y = []
for c, x in zip(classes, X):
    model = cluster.Birch(n_clusters=c)
    model.fit(x)
    if hasattr(model, "labels_"):
        y.append(model.labels_.astype(np.int))
    else:
        y.append(model.predict(x))
        
fig = plt.figure(figsize=(27, 9))
fig.suptitle("Birch", fontsize=48)
for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    ax.scatter(X[i][:,0], X[i][:,1], c=y[i])
    
plt.savefig("Birch.eps", format="eps")

# =============================================================================

y = []
for c, x in zip(classes, X):
    model = cluster.SpectralClustering(n_clusters=c, affinity="nearest_neighbors")
    model.fit(x)
    if hasattr(model, "labels_"):
        y.append(model.labels_.astype(np.int))
    else:
        y.append(model.predict(x))
        
fig = plt.figure(figsize=(27, 9))
fig.suptitle("SpectralClustering", fontsize=48)
for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    ax.scatter(X[i][:,0], X[i][:,1], c=y[i])

plt.savefig("SpectralClustering.eps", format="eps")

# =============================================================================

y = []
for c, x in zip(classes, X):
    model = mixture.GaussianMixture(n_components=c, covariance_type="full")
    model.fit(x)
    if hasattr(model, "labels_"):
        y.append(model.labels_.astype(np.int))
    else:
        y.append(model.predict(x))
        
fig = plt.figure(figsize=(27, 9))
fig.suptitle("GaussianMixture", fontsize=48)
for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    ax.scatter(X[i][:,0], X[i][:,1], c=y[i])

plt.savefig("GaussianMixture.eps", format="eps")

# =============================================================================

y = []
for c, x in zip(classes, X):
    model = cluster.OPTICS(min_samples=20, xi=0.05, min_cluster_size=0.1)
    model.fit(x)
    if hasattr(model, "labels_"):
        y.append(model.labels_.astype(np.int))
    else:
        y.append(model.predict(x))
        
fig = plt.figure(figsize=(27, 9))
fig.suptitle("OPTICS", fontsize=48)
for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    ax.scatter(X[i][:,0], X[i][:,1], c=y[i])

plt.savefig("OPTICS.eps", format="eps")

# =============================================================================

y = []
eps = [0.3, 0.3, 0.3, 0.3, 0.15, 0.18]
for c, x, e in zip(classes, X, eps):
    model = cluster.DBSCAN(eps=e)
    model.fit(x)
    if hasattr(model, "labels_"):
        y.append(model.labels_.astype(np.int))
    else:
        y.append(model.predict(x))
        
fig = plt.figure(figsize=(27, 9))
fig.suptitle("DBSCAN", fontsize=48)
for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    ax.scatter(X[i][:,0], X[i][:,1], c=y[i])

plt.savefig("DBSCAN.eps", format="eps")

# =============================================================================


