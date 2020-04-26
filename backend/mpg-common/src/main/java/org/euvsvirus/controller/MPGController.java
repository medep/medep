package org.euvsvirus.controller;

import java.util.List;

import org.euvsvirus.entity.Dataset;
import org.springframework.http.ResponseEntity;

public interface MPGController {

	ResponseEntity<List<Dataset>> getAllData();
}
