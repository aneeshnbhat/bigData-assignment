import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
//import org.json.JSONTokener;
//import org.json.JSONException;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.time.LocalDate;
import java.lang.Math;

public class PlaneTwo {

	private static boolean isValidWord(String str) {
		if(str!=null) {
			char[] charArr = str.toCharArray();
			for(int i=0;i<charArr.length;i++) {
				if((charArr[i]<'a' || charArr[i]>'z') && (charArr[i]<'A' || charArr[i]>'Z') && charArr[i] != ' ') {
					return false;
				}
			}
			return true;
		} else {
			return false;
		}
	
	}
	
	private static boolean isValidRecognized(String str) {
		if(str !=null &&(str.equals("true") || str.equals("false"))) {
			return true;
		}
		return false;
	}

	private static boolean isValidCountryCode(String str){
		
		if(str!=null && str.length()==2) {
			char[] charArr = str.toCharArray();
			for(int i=0;i<charArr.length;i++) {
				if(!Character.isUpperCase(charArr[i])) {
					return false;
				}
			}
			return true;
		} else {
			return false;
		}
	}
	
	private static boolean isValidKeyId(String str) {
		if(str!=null && str.length()==16){
			return true;
		}
		return false;
	}
	
	// checks if the drawing is valid and distance b/w 0th coordinates of 1st stroke from origin is greater than the
	// given distance
	private static boolean isValidDrawing(JSONArray arr,Double distance) {
		if(arr!=null && arr.size()>=1) {
			for(int i=0;i<arr.size();i++) {
				JSONArray arr1 = (JSONArray)arr.get(i);
				if(arr1.size()!=2){
					return false;
				}
			}
			JSONArray arr1 = (JSONArray)arr.get(0);
			JSONArray arrX = (JSONArray)arr1.get(0);
			JSONArray arrY = (JSONArray)arr1.get(1);
			long x =0;
			long y =0;
			if(arrX != null && arrY != null) {
				x = (Long)arrX.get(0);
				y = (Long)arrY.get(0);
				if(Math.sqrt(Math.pow(x,2) + Math.pow(y,2) + 1.0) > distance) {
					return true;
				}
			} 
			return false;
		} else {
			return false;
		}
		
	}


  public static class PlaneMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    //private Text word = new Text();
    
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
		
		Configuration conf = context.getConfiguration();
		//JSONTokener jsonTokener = new JSONTokener(value.toString());
		JSONParser jsonParser = new JSONParser();
		try{	
			JSONObject jsonObject = (JSONObject) jsonParser.parse(value.toString());
			String aircraftName = conf.get("aircraftName");
			Integer distance = Integer.parseInt((String)conf.get("distance"));
			//aircraftName = aircraftName.toLowerCase();
			//String aircraftName = new String("airplane");			

			String aircraft = (String)jsonObject.get("word");		
			//aircraft = aircraft.toLowerCase();
			String dateTime = (String)jsonObject.get("timestamp");
			String dateOnly = dateTime.split(" ")[0];
			String[] dateArr = dateOnly.split("-");
			int yyyy = Integer.parseInt(dateArr[0]);
			int mm = Integer.parseInt(dateArr[1]);
			int dd = Integer.parseInt(dateArr[2]);
			

			if(aircraftName != null && aircraftName.equals(aircraft)) {
				String recognized = ((Boolean)jsonObject.get("recognized")).toString();
				
				LocalDate date = LocalDate.of(yyyy,mm,dd);
				int dateInt = date.getDayOfWeek().getValue();
				
				boolean isvalidWord = isValidWord(aircraft);
				boolean isvalidRecognized = isValidRecognized(recognized);
				boolean isvalidCode = isValidCountryCode((String)jsonObject.get("countrycode"));
				boolean isvalidKey = isValidKeyId((String)jsonObject.get("key_id"));
				boolean isvalidDrawing = isValidDrawing((JSONArray)jsonObject.get("drawing"), new Double(distance));

				if(isvalidWord && isvalidRecognized && isvalidCode && isvalidKey && isvalidDrawing){
					context.write(new Text((String)jsonObject.get("countrycode")), one);
				}
				
							
			}			

		}catch(ParseException e) {
			e.printStackTrace();
		}
    }
  }

  public static class PlaneReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    conf.set("aircraftName",args[2]);
    conf.set("distance",args[3]);
    conf.set("mapred.textoutputformat.separator",",");
    
    Job job = Job.getInstance(conf, "planeTwo");
    job.setJarByClass(PlaneTwo.class);
    job.setMapperClass(PlaneMapper.class);
    job.setCombinerClass(PlaneReducer.class);
    job.setReducerClass(PlaneReducer.class);	
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    
    

    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
