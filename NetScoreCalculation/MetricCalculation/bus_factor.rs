/*  Name: Jack Kwan
 *  Date of Last Edit: 2/12/2023
 *  
 *  Purpose: Calculate Bus Factor Sub Metric of a given Github Repository
 *
 *  Details: Using provided data, calculates the Busfactor in the range of [0,1], with 1 being each contributor being most valuable upon replacement 
*/
use std::env;

//calculate_busfactor will determine the Bus Factor weighting for the Net Score total
pub fn calculate_busfactor(numcommits: f64, numcontributors: f64, numfiles: f64) -> f64{

    let mut busfactor: f64 = 0.0;
    busfactor = (0.5) * ((numcontributors / numcommits) + (numcontributors / numfiles)); //Calculate the score as an average between two metrics
    if busfactor > 1.0 {
        return 1.0;
    }
    else {
        return f64::trunc(busfactor * 100.0) / 100.0;
    }   
}

fn main(){
    let args : Vec<String> = env::args().collect();                                     //Input the arguments into vector args
    let numberofcommits : f64 = args[1].parse().unwrap();                               //Converts the string values into a f64 value 
    let numberofcontributors : f64 = args[2].parse().unwrap();
    let numberoffiles : f64 = args[3].parse().unwrap();

    let contributor_score = calculate_busfactor(numberofcommits, numberofcontributors, numberoffiles);
    println!("Contributors weighting: {contributor_score}");
}