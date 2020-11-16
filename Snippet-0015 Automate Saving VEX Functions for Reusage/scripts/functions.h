void noiseremove(int ptnum; float sc, seed, th){
    vector pos = point(0, "P", ptnum);
    float noiseval = noise(pos * sc + seed);
    if(noiseval < th){
        removepoint(0, ptnum);
    }
}