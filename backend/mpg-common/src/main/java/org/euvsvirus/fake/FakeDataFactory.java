package org.euvsvirus.fake;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import org.euvsvirus.dao.DataObject;
import org.euvsvirus.entity.Attribute;
import org.euvsvirus.entity.Dataset;
import org.springframework.stereotype.Service;

@Service
public class FakeDataFactory {

	private static List<String> PEOPLE = Arrays.asList("Jim Halpert", "Pam Beesly", "Stanley Hudson", "Angela Martin",
			"Phyllis Vance", "Meredith Palmer", "Creed Bratton", "Oscar Martinez", "Ryan Howard", "Kelly Kapoor",
			"Toby Flenderson", "Michael Scott", "Darryl Philbin", "Erin Hannon", "Gabe Lewis", "Jan Levinson",
			"David Wallace", "Roy Anderson", "Karen Filippelli", "Bob Vance", "Hank Doorman", "Holly Flax",
			"Todd Packer", "Dwight Schrute");

	private static List<String> DATASET_NAMES = Arrays.asList("COVID-19 clinical study", "Breast cancer study",
			"Staphylococcus aureus study", "Chronic kidney disease", "Alzheimer's disease");

	private static List<String> ATTRIBUTE_NAMES = Arrays.asList("Age", "Gender", "Lives in Retirement Home",
			"Arterial Hypertension", "Diabetes", "Coronary Disease", "Prior AMI/CVI", "Hearth Failure",
			"Chronic Kidney Disease", "Obesity", "Asthma", "Compromised Immune System", "Malignant Disease",
			"Contact with Diseased", "ACIE Therapy", "ARB Therapy", "Fever (>37.5)", "Cough", "Breathing Problems",
			"Fatigue", "Headache", "Breast Pain", "Muscle/Joint Pain", "Changed Smell/Taste", "Sore Throat",
			"Stuffed Nose", "Diarrhea", "Night Sweating", "Nausea", "Runny Nose", "Body Temperature",
			"Breathing Frequency", "Blood Pressure High", "Blood Pressure Low", "O2 Saturation", "Additional O2", "AF",
			"AST", "ALT", "LDH", "CRP", "Lkci", "Hb", "Ht", "Trombo", "Neutrophils ", "lymphocytes ", "pH", "pCO2",
			"pO2", "D-dimer", "Infiltrates", "Hospitalisation", "Needs O2", "Intensive treatment", "Needs ventilator",
			"Treatment duration", "Survived");

	private static List<String> ATTRIBUTES_NUMERIC = Arrays.asList("Body Temperature", "O2 Saturation", "AF", "AST",
			"ALT", "LDH", "CRP", "Lkci", "Hb", "Ht", "Trombo", "Neutrophils ", "lymphocytes ", "pH", "pCO2", "pO2",
			"D-dimer", "Treatment duration");

	private static List<String> ATTRIBUTES_DECIMAL = Arrays.asList("Age", "Breathing Frequency", "Treatment duration",
			"Blood Pressure High", "Blood Pressure Low");

	private static List<Dataset> DATASETS;

	private static Random RND = new Random();

	public static List<Dataset> getAllMetadata() {

		if (DATASETS != null)
			return DATASETS;

		List<Dataset> lst = new ArrayList<>();
		Dataset d;
		for (int i = 0; i < DATASET_NAMES.size(); i++) {
			d = new Dataset();
			d.setID(i);
			d.setDatasetName(DATASET_NAMES.get(i));
			d.setAuthors(getRandomPeople());
			d.setOwners(getRandomPeople());
			d.setData(getRandomDataObject());

			lst.add(d);
		}

		DATASETS = lst;
		return lst;
	}

	static List<String> getRandomPeople() {
		return getRandom(PEOPLE);
	}

	static List<Attribute> getRandomAttributes() {
		List<String> lst = getRandom(ATTRIBUTE_NAMES);
		List<Attribute> retlist = new ArrayList<>();

		lst.forEach(s -> retlist.add(new Attribute(s, getAttributeType(s))));

		return retlist;
	}

	static String getAttributeType(String attributeName) {
		if (ATTRIBUTES_NUMERIC.contains(attributeName))
			return "numeric";
		else if (ATTRIBUTES_DECIMAL.contains(attributeName))
			return "decimal";
		else
			return "nominal";
	}

	static List<Object> getRandomData(List<Attribute> attributes) {

		List<Object> val = new ArrayList<>();
		int cnt = RND.nextInt(50);

		do {
			List<Object> row = new ArrayList<>();
			for (Attribute att : attributes) {

				switch (att.getAttributeType()) {
				case "numeric":
					row.add(RND.nextFloat()*RND.nextInt(10));
					break;
				case "decimal":
					row.add(RND.nextInt(100));
					break;
				default:
					row.add(RND.nextBoolean() ? 1 : 0);
					break;
				}
			}

			val.add(row);

		} while (val.size() < cnt);

		return val;
	}

	static List<String> getRandom(List<String> items, Integer... count) {
		List<String> people = new ArrayList<>();
		int cnt = -1;
		if (count.length > 0) {
			cnt = count[0].intValue();
		} else {
			cnt = RND.nextInt(items.size());
		}

		do {
			int idx = RND.nextInt(items.size());
			if (!people.contains(items.get(idx))) {
				people.add(items.get(idx));
			}
		} while (people.size() < cnt);

		return people;
	}

	static DataObject getRandomDataObject() {
		DataObject ds = new DataObject();

		ds.setAttributes(getRandomAttributes());
		ds.setData(getRandomData(ds.getAttributes()));

		return ds;
	}
}
