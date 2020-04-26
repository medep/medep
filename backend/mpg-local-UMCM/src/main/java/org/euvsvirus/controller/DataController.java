package org.euvsvirus.controller;

import java.util.List;

import org.euvsvirus.UMCMService;
import org.euvsvirus.entity.Dataset;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/data", produces = "application/json")
public class DataController implements MPGController {

	@Autowired
	public UMCMService service;

	@Override
	@GetMapping(path = { "", "/" })
	public ResponseEntity<List<Dataset>> getAllData() {

		List<Dataset> allData = service.getAllData();

		return ResponseEntity.ok(allData);
	}
}
